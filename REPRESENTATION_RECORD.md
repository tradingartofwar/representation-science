# Representation Record

A Representation Record is the smallest standard research artifact in this project.

## Template

```text
Record ID:
Date:
Laboratory:
Underlying system / reality:
Domain and assumptions:

Question:
Requested output:
Next operation, if relevant:

Representation name/version:
Representation object:
Information retained:
Information omitted:

Recovery source:
Recovery / translation map:
Can omitted information be reconstructed exactly?:

Adequacy claim:
Claim status:
Evidence:
Counterchecks:

Known failure / falsification condition:
Observed failure, if any:
What distinction became consequential:

Representation cost:
Recovery cost:
Costs not measured:

Future questions still supported:
Future questions requiring reopening/enrichment:

Source pointers:
Notes:
```

## Rules

The record is question-specific. Never say a representation is adequate without saying adequate **for what**.

Information omitted is not automatically information lost. If it is exactly recoverable from a pinned source, record that distinction.

A richer representation is not automatically better. It earns its cost when the retained structure supports an operation the smaller representation cannot safely support, or when preserving optionality is itself the declared objective.

A failure should identify the smallest known missing distinction rather than merely label the representation insufficient.

Possible cost dimensions include object count, dimension/rank, symbolic size, construction time, query time, recovery operations, proof obligations, and human inspection burden.

Do not invent one scalar representation-complexity score until evidence shows that combining these dimensions is useful.
