---
Title: Make skills phase aware proportional and consistent across long sessions
Ticket: SKILLS-FRICTION-001
Status: active
Topics: [documentation, tooling]
DocType: index
Intent: long-term
Owners: []
RelatedFiles: []
ExternalSources: []
Summary: Research delivered; implementation remains open for conflicting policies, proportional diary modes, compact resume and evidence-aware validation.
LastUpdated: 2026-09-10T15:37:22Z
WhatFor: Improve actual agent instruction behavior using verified session evidence.
WhenToUse: Reviewing or implementing process skill changes.
---

# Skills workflow friction

The intern guide analyzes the original session's actual skill loads and instruction text, not just a qualitative recollection. It identifies a confirmed upload-policy conflict, diary/resume overhead and limits in the analysis heuristics themselves.

## Documents and evidence

- [Intern analysis, design and implementation guide](design-doc/01-intern-guide-to-phase-aware-skills-and-evidence-proportional-workflows.md)
- [Investigation diary](reference/01-investigation-diary.md)
- [Tasks](tasks.md) and [changelog](changelog.md)
- [Selected session evidence](sources/session-evidence.json)
- [Verified counts and metric corrections](sources/evidence-summary.json)

## Scope and status

The requested research documents are complete. Existing skills were not rewritten; their implementation tasks remain open. Pre-existing modifications and untracked files were preserved. The full frozen transcript/normalized archive is outside Git; only selected evidence, query results and provenance are stored here.

Companion: **DOCMGR-FRICTION-001**, rooted at `/home/manuel/code/wesen/go-go-golems/docmgr/ttmp/2026/09/10/DOCMGR-FRICTION-001--reduce-documentation-workflow-friction-with-deterministic-writes-and-coherent-milestones`. It owns deterministic document mutation and proposed milestone/resume APIs.

## Delivery

The reMarkable bundle destination is `/ai/2026/09/10/SKILLS-FRICTION-001`. Dry-run, upload and verification receipts are retained under `sources/`; the upload result is authoritative for delivery status. The bundle contains the guide and investigation diary, with rendered diagrams.
