# Evidence levels

Choose preservation proportional to the claim, not the length of the process checklist.

- **Routine success:** command, result/exit status and relevant revision or commit. A readable normalized success log is enough; disclose formatting normalization if relevant. Do not gzip decorative whitespace merely to retain a routine doctor result.
- **Experiment:** configuration, versions, inputs, observations, interpreted measurements and reproduction steps. Distinguish simulation from actual runtime evidence. Retain raw diagnostics when they materially support interpretation.
- **Failure investigation:** exact relevant command/error, context, hypothesis, attempted recovery and what resolved it. Do not summarize away ordering or partial-success effects.
- **Byte-identity claim:** retain hashes and original bytes where the contract requires it. A normalized log cannot prove raw-byte equality.

Evidence is not a completion oracle. Map each explicit requirement to a real artifact and its scope; unresolved uncertainty stays open. Do not lower validation coverage to improve a tool-count metric.
