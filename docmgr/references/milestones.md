# Milestone and resume commands

Use a verified binary exposing these commands. The DOCMGR-FRICTION-001 implementation uses Glazed v1.3.6; structured output is `--with-glaze-output --output json`. Check help on a different installed version rather than guessing.

```bash
docmgr milestone record --ticket ID --operation-id persistence-reviewed \
  --summary 'Reviewed persistence tests' --phase validate \
  --task-id ab12 --next 'Review HTTP parity' --dry-run
# Remove --dry-run to apply after review.
docmgr ticket resume --ticket ID --with-glaze-output --output json
```

Milestone record updates selected stable task IDs and changelog, and persists a bounded request/receipt. It does not author diary prose or infer completion. Valid phases: start, implement, validate, checkpoint, resume, close. The structured milestone row has `receipt`; the resume row has `resume`. Preserve that wrapper when parsing CLI output.

Optional `--evidence-file` accepts a JSON array of `kind`, `path`, `revision`, `claim`. Paths must resolve within the ticket (`doc://sources/test.log`, for example); revision is actual file SHA256, not a Git hash. Store ticket-local summaries referencing external commits rather than expecting unrestricted file access. `--expected-file` accepts current projection hashes for index.md/tasks.md/changelog.md; resume provides those revisions.

Same ID/same request returns the original receipt. Changed payload under an existing ID fails. Pending journals block unrelated operations. Retry the original ID/request to recover; conflicting external edits require deliberate reconciliation. Never remove a pending journal simply to proceed.

Close and milestone share cooperative locking and process-crash recovery, not atomic multi-file visibility or power-loss durability. Legacy commands and external editors do not share the lock. Resume is a read-only derived view that reports remaining tasks, current revisions, document pointers, pending operations and stale evidence. Its phase is advisory; current user instructions and actual files remain authoritative.

For full limits, platform support, failure boundaries and HTTP parity, read `docmgr help milestone-workflows`. Do not archive successful boilerplate logs as raw-byte research unless their bytes are themselves evidence.
