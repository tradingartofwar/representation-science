#!/usr/bin/env python3
"""Fetch only the public, hash-pinned qualification inputs. No installation."""
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

manifest = json.loads(Path(__file__).with_name("SOURCES.json").read_text())
cache = Path(sys.argv[1]).resolve()
for item, directory in [(manifest["tzdata"], cache)] + [(x, cache / "wheels") for x in manifest["wheels"]]:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / item["filename"]
    if path.exists():
        data = path.read_bytes()
    else:
        with urllib.request.urlopen(item["url"], timeout=30) as response:
            data = response.read(item["bytes"] + 1)
    if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
        raise ValueError(f"Source identity mismatch: {item['filename']}")
    path.write_bytes(data)
    print(item["filename"], item["sha256"])
