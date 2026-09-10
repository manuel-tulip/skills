# Diary workflow reference

The canonical formats now live in [investigation-entry.md](investigation-entry.md) and [milestone-entry.md](milestone-entry.md); evidence preservation lives in [evidence-levels.md](evidence-levels.md). This reference intentionally does not duplicate those templates.

Use investigation mode for substantive work and explicit detailed-diary requests. Milestone mode avoids manufacturing a full debugging narrative for routine success. Both retain prompt provenance, outcomes, evidence and continuation pointers.

Create a ticket diary with `docmgr doc add --ticket ID --doc-type reference --title Diary`. Relate primary code/evidence with absolute `--file-note "path:reason"` arguments. Record a coherent implementation milestone, validate affected behavior, and commit focused changes. A later diary checkpoint can cite the code commit; two separate commits for each tiny edit are not required.

Historical diaries keep their original schema and failures. These conventions apply to new entries; do not rewrite old history to make the workflow appear cheaper. When resuming, start at the latest relevant checkpoint and expand earlier details only as needed, subject to higher-priority instructions.
