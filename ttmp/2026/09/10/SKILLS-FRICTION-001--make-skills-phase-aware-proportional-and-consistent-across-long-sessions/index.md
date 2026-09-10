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
Summary: Implemented coherent upload policy, diary modes, phase/resume guidance and tested workflow helpers; real post-adoption session comparison remains open.
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

Policy, diary, resume and helper implementation is committed at `112f8aa` and `acb7338`, with ten passing tests and a clean owned-skill convention check. The remaining task `vewh` requires equivalent real post-adoption sessions; synthetic fixtures are not evidence of time/token savings. Pre-existing modifications and untracked files were preserved. Research snapshots remain historical and the full frozen archive stays outside Git. See the diary and `sources/implementation-validation.json`.

Companion: **DOCMGR-FRICTION-001**, rooted at `/home/manuel/code/wesen/go-go-golems/docmgr/ttmp/2026/09/10/DOCMGR-FRICTION-001--reduce-documentation-workflow-friction-with-deterministic-writes-and-coherent-milestones`. It owns deterministic document mutation and the implemented milestone/resume APIs.

## Delivery

The original research delivery (not a new implementation upload) used the reMarkable bundle destination `/ai/2026/09/10/SKILLS-FRICTION-001`. Dry-run, upload and verification receipts are retained under `sources/`; the upload result is authoritative for delivery status. The bundle contains the guide and investigation diary, with rendered diagrams.
