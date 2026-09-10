---
Title: Investigation diary
Ticket: SKILLS-FRICTION-001
Status: active
Topics:
    - documentation
    - tooling
DocType: reference
Intent: long-term
Owners: []
RelatedFiles:
    - Path: repo://diary/SKILL.md
      Note: Detailed and milestone diary modes
    - Path: repo://remarkable-upload/SKILL.md
      Note: Single delivery policy owner
    - Path: repo://ticket-research-docmgr-remarkable/SKILL.md
      Note: Phase-aware orchestration
    - Path: repo://ticket-research-docmgr-remarkable/scripts/workflow_checks.py
      Note: Policy, dependency and resume checks
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/design-doc/01-intern-guide-to-phase-aware-skills-and-evidence-proportional-workflows.md
      Note: Primary research handoff
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/scripts/01-session-evidence.sql
      Note: Targeted normalized evidence query
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/scripts/02-evidence-summary.py
      Note: Verified counts and correction ledger
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/sources/implementation-validation.json
      Note: Full committed instruction inventory and test evidence
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/sources/remarkable-upload.log
      Note: Verified delivery result
ExternalSources: []
Summary: Session-specific instruction conflict investigation and evidence limitations.
LastUpdated: 2026-09-10T15:37:22Z
WhatFor: Preserve the investigation and guide future skill edits.
WhenToUse: Resuming the skill-improvement implementation phases.
---


# Investigation diary

## Goal

Turn the actual Video Observatory session into concrete skill improvements without weakening required validation or changing unrelated work.

## Step 1: Identify instruction conflicts and verify session evidence

Initialized docmgr in this skills repository and created the requested ticket. Used the analysis skills' own query tools, then checked their output against actual tool records and the native snapshot instead of treating heuristic counts as a verdict.

### Prompt Context

**User prompt (verbatim):**

> ok, create a new docmgr ticket in ~/code/wesen/go-go-golems/docmgr itself about improving docmgr, and another one about improving the skills in ~/.pi/agent/skills (which is a git repo) itself.
>
> In both cases, Create  a detailed analysis / design / implementation guide that is for a new intern, explaining all the parts of the system needed to understand what it is, with prose paragraphs and bullet point sand pseudocode and diagrams and api references and file references. It should be very clear and technical. Store in the ticket and the nupload to remarkable.
>
> Cross reference the things if necessary. Do go into the details of this session in particular, reference which skills and other guidance was wrong specifically, etc...
>
> [REMINDER] Output a <summary>...</summary> block at the VERY END of your response. This is mandatory.

**Assistant interpretation:** Produce a researched implementation guide and reMarkable delivery, leaving proposed skill rewrites for subsequent implementation.

**Inferred user intent:** Replace vague criticism of administrative overhead with specific file-level, testable improvements.

### What I did

- Preserved existing Git changes and initialized only the requested documentation workspace.
- Copied the native session to an isolated snapshot, fingerprinted it and converted only that source.
- Ran five docmetrics profiles and a targeted normalized SQL query.
- Read actual returned skill text at original turn 4, confirmed the upload conflict, and inspected EOF errors and later skill reloads.
- Read installed Pi skills documentation and wrote a phase-aware design with explicit ownership and acceptance fixtures.

### Why

The earlier qualitative ranking was not measured time attribution. This guide needs stronger evidence and explicit corrections wherever the profile itself is misleading.

### What worked

The original skill loads contain both conflicting reMarkable workflows. Before post-mortem turn 1505, explicit reads include diary six times and docmgr/textbook/vault skills five times each. The native snapshot has six compaction records. Cross-checks tied EOF repairs to source commits and the original final diary.

### What didn't work

The profile reports zero ticket reads/help consumption despite inspected counterexamples, and cache-collapse candidates are not a reliable compaction count. Those fields are retained as heuristic output but excluded from causal claims. The repository had no `ttmp` workspace initially; initialization was expected setup, not a product failure. Its freshly generated `_guidelines/skill.md` and `_templates/skill.md` also failed the staged blank-EOF check. A partial exact replacement left another trailing blank; normalized only those newly generated files to one final LF. Existing live skills were not altered. Routine human help/doctor captures were normalized separately from unchanged experiment and transcript JSON.

### What I learned

Some overhead comes from conflicting content that was successfully loaded, contradicting an overly categorical older interpretation that skill delivery rather than content is always the problem. Current base transcript guidance and older adapter warnings must be version-scoped.

### What was tricky to build

Separating mandatory higher-priority instructions from skill-local recommendations, and differentiating a real contradiction from broad-but-compatible guidance. Repeated reads are observable; exact time wasted is not established. Shared inode identity across skill locations requires link-topology inspection before implementation edits.

### What warrants a second pair of eyes

The instruction ownership matrix, snapshot cutoff, metric corrections, distinction between proposed and existing APIs, and whether any suggested reduction would lose user-required evidence.

### What should be done in the future

Implement the open skill phases with composed workflow fixtures and compare future sessions on equivalent tasks. Do not use lower tool counts as the sole success metric.

### Code review instructions

Read the guide, selected session evidence, evidence-summary script and guidance line map. Reproduce the query with go-minitrace and compare against the retained snapshot hash. Do not modify native session files or stage pre-existing skill edits.

### Technical details

Original session: `01a0837a-fb1c-7183-9bf5-26fce6d60551`. Full archives remain outside Git under `/tmp/doc-friction-session`; selected evidence and provenance are committed with the ticket. The active pinned research workflow and specialist upload skill still conflict; this task documents that conflict rather than silently changing the policy. Delivery followed the explicit pinned research workflow, including dry-run and remote listing: `SKILLS-FRICTION-001 Intern Guide` was uploaded to `/ai/2026/09/10/SKILLS-FRICTION-001`. Both diagrams were inspected and the wider phase diagram narrowed. The exact uploaded diary is retained in `sources/print/diary.md`; this delivery note was added afterward. The requested `.pi/agent/skills` path resolves to `/home/manuel/.codex/skills`, explaining canonical paths in docmgr output; the same Git repository was used throughout.

## Step 2: Implement coherent policy ownership, diary modes and workflow checks

The implementation makes the upload specialist the single owner of mechanics and success evidence, while the research core selects phases and delegates rather than duplicating commands. Detailed implementation diaries retain the full investigation format; ordinary success checkpoints can use a smaller mode without inventing debugging narrative.

The new helpers check explicit local-reference and policy conventions, derive dependency keys and require review attestations for every recognized figure. They do not enforce arbitrary natural-language instructions or prove that future agents will behave more efficiently. The new docmgr integration is based on the locally built, exercised commands rather than the earlier proposed API sketches.

### Prompt Context

**User prompt (verbatim):**

> let's actually build it all. commit at appropriate intervals and keep a detailed diary as you work (using the diary format from the skill).
>
> [REMINDER] Output a <summary>...</summary> block at the VERY END of your response. This is mandatory.

**Assistant interpretation:** Implement the researched skill changes and companion tooling while keeping a detailed diary and focused commits.

**Inferred user intent:** Reduce contradictory instructions and repeated administrative work without sacrificing evidence, review or user requirements.

**Commit (code/instructions):** `112f8aa` — "feat: make research skills phase aware and evidence proportional"

### What I did
- Replaced unconditional upload preflight/listing prohibitions and requirements with one specialist-owned policy, including explicit-user overrides, overwrite protection and bounded auth retry.
- Split diary modes into canonical milestone/investigation references and an evidence-level reference; redirected the old workflow reference instead of leaving duplicate templates.
- Added start/implement/checkpoint/resume/close guidance and verified docmgr milestone/resume usage.
- Version-scoped transcript adapter claims, corrected heuristic compaction interpretation and gated implementation on the actual user request.
- Added standard-library policy/reference checks, dependency-aware validation keys, all-figure attestation checks, resume shape checks and a comparable-session evaluation helper.

### Why
- A lower-level skill must not contradict an explicit user verification request, silently change user pins, or pretend custom phase prose creates a runtime loader.
- Fewer calls are not an improvement if failures disappear from the diary or required checks are skipped.

### What worked
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts -p 'test_workflow_checks.py' -v` passes all nine tests, including multiple composed policy cases and negative fixtures.
- `python3 scripts/workflow_checks.py skills` reports no errors.
- Checks reject a broken local link, a reintroduced orchestrator upload command, incomplete second-diagram review, missing assets, path escape and non-comparable evaluation inputs.
- Unchanged dependencies stay cached; changed asset affects its document; changed renderer/policy/stylesheet invalidates all dependent documents.

### What didn't work
- No skill/helper test failures observed in this step. There is no controlled future-agent benchmark yet; fixture success is not presented as a token/time reduction measurement.

### What I learned
- Current-file instructions and current-session pinned instructions differ: editing a skill does not retroactively replace higher-priority content already in context. This session therefore continues the explicitly requested detailed format.
- The installed Pi skills documentation confirms progressive disclosure but does not implement phase semantics from custom metadata.

### What was tricky to build
- Both orchestration and specialist references needed updating to remove the actual contradiction. Fixing only the visible top-level command block would leave the checklist inconsistent.
- The diagram checker must distinguish a cache key from competent review: attested checks are explicit, and renderer/policy changes invalidate prior keys. The helper recognizes fenced Mermaid and inline Markdown images, not every possible renderer extension.
- The requested .pi and .claude diary paths retained inode 67397783 before/after edits, confirming shared-directory identity was preserved.

### What warrants a second pair of eyes
- Natural-language instruction composition still needs review beyond known-pattern checks.
- User-required validation and full-read instructions always override the reduced defaults.
- Resume validation checks shape, not the actual files; visual attestations and curated session metrics require truthful evidence.

### What should be done in the future
- Collect equivalent post-adoption sessions and use the comparison helper with frozen provenance. Task vewh remains open until that real evidence exists; synthetic policy tests do not satisfy it.

### Code review instructions
- Review upload and research core/checklist changes together, then diary references and docmgr integration.
- Run the nine tests and skills checker from `ticket-research-docmgr-remarkable`.
- Check the pre-existing go-minitrace skill changes remain unstaged and byte-identical to the saved starting hashes.

### Technical details
- Native session stores and the original research snapshot remain untouched.
- `sha256sum -c /tmp/friction-preserved-skill-hashes` passed for both pre-existing modified go-minitrace files.
- No extension, user pin or global model setting was changed; phase selection is an instruction convention.

## Step 3: Keep validation-state persistence itself proportional

Final review applied the same no-op principle to the new dependency cache: recording identical validation state should not rewrite its file or change mtime. A fully cached run also does not need a new reviews file; actual changed documents still require complete attestations.

### Prompt Context
**User prompt (verbatim):** (see Step 2)

**Assistant interpretation:** Remove avoidable mutation from the newly introduced helper before handoff.

**Inferred user intent:** Ensure the workflow improvements do not recreate the bookkeeping problem they address.

**Commit (code):** `acb7338` — "fix: avoid rewriting unchanged workflow validation state"

### What I did
- Added write-if-changed state persistence and optional reviews input for unchanged plans.
- Added a sentinel-mtime regression.

### Why
- Dependency caching should avoid both repeated rendering and meaningless state rewrites.

### What worked
- All ten tests pass, including unchanged-state mtime preservation and changed-state updates.

### What didn't work
- No test failures observed in this step.

### What I learned
- Administrative artifacts need the same no-op discipline as product metadata.

### What was tricky to build
- Omitting new review input is safe only for cached documents; changed dependencies still fail without check success and every recognized figure attested.

### What warrants a second pair of eyes
- Review cache invalidation and attestation requirements together, not just write suppression.

### What should be done in the future
- Collect comparable real sessions for task vewh; no synthetic fixture is promoted to a measured efficiency result.

### Code review instructions
- Inspect `write_state`, the record command and the mtime test. Run the ten-test helper suite.

### Technical details
- State bytes are compared before writing. Existing valid cached reviews are reused; missing changed-document reviews remain an error.
- Used the new docmgr milestone command on this real ticket to complete lic8/bprx/ymgw with the validation manifest as SHA256-bound evidence. Resume reports only vewh remaining, no conflicts, and doctor passes. The helper validates both this resume response and the companion completed docmgr ticket. The operational receipt and journal are retained; no new reMarkable upload or Git push was requested.
