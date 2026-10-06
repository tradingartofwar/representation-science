"""Isolation, declared limits and artifact integrity; no task answer computation."""
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text())


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def write(path, obj):
    encoded = (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode()
    if len(encoded) > read("config.json")["budgets"]["output_file_bytes"]:
        raise RuntimeError("artifact size budget exceeded")
    path.write_bytes(encoded)


def check_environment(config):
    actual = {"implementation": platform.python_implementation(), "python_version": platform.python_version(),
              "system": platform.system(), "machine": platform.machine()}
    if actual != config["runtime"]:
        raise RuntimeError(f"runtime mismatch: {actual}")
    return {**actual, "python_build": sys.version,
            "python_executable_sha256": hashlib.sha256(Path(sys.executable).read_bytes()).hexdigest()}


def verify_manifest():
    manifest = read("MANIFEST.json")
    for relative, expected in manifest["sha256"].items():
        path = ROOT / relative
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"manifest mismatch: {relative}")
    return hashlib.sha256((ROOT / "MANIFEST.json").read_bytes()).hexdigest()


@contextmanager
def deadline(seconds):
    def expired(signum, frame):
        raise TimeoutError("reference/construction wall budget exceeded")
    previous = signal.signal(signal.SIGALRM, expired)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def invoke(arm, payload, local, config):
    limits = config["budgets"]
    def restrict():
        resource.setrlimit(resource.RLIMIT_AS, (limits["worker_memory_bytes"],) * 2)
        resource.setrlimit(resource.RLIMIT_CPU, (limits["worker_cpu_seconds"],) * 2)
        resource.setrlimit(resource.RLIMIT_FSIZE, (limits["worker_output_bytes"],) * 2)
        resource.setrlimit(resource.RLIMIT_NOFILE, (limits["maximum_open_files"],) * 2)
    encoded = canonical({"arm": arm, "payload": payload, "request": {"local": local}}).encode()
    start = time.perf_counter()
    cpu_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with tempfile.TemporaryDirectory(prefix="exp002-worker-") as temporary:
        script = Path(temporary) / "worker.py"
        script.write_bytes((ROOT / "worker.py").read_bytes())
        # Only this code file is staged. No payload store, references or cases are copied.
        result = subprocess.run([sys.executable, "-I", str(script)], input=encoded,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=temporary,
                                env={"PATH": os.defpath, "LANG": "C.UTF-8", "TZ": "UTC"},
                                preexec_fn=restrict, timeout=limits["worker_wall_seconds"])
    elapsed = time.perf_counter() - start
    cpu_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    raw = {"stdout": result.stdout.decode(), "stderr": result.stderr.decode(), "returncode": result.returncode}
    if result.returncode or result.stderr or len(result.stdout) > limits["worker_output_bytes"]:
        raise RuntimeError("WORKER_FAILURE " + canonical(raw))
    packet = json.loads(result.stdout)
    if packet["access"] != {"external_source_reads": 0, "denied_events": []}:
        raise RuntimeError("UNDECLARED_ACCESS " + canonical(packet))
    return {"arm": arm, "local": local, **raw, **packet,
            "measurement": {"wall_seconds": elapsed,
                            "child_cpu_seconds": cpu_after.ru_utime + cpu_after.ru_stime - cpu_before.ru_utime - cpu_before.ru_stime,
                            "stdin_bytes": len(encoded), "stdout_bytes": len(result.stdout),
                            "canonical_response_bytes": len(canonical(packet["response"]).encode()),
                            "canonical_payload_bytes": len(canonical(payload).encode())}}
