---
title: "Intern guide to phase aware skills and evidence proportional workflows"
Title: Intern guide to phase aware skills and evidence proportional workflows
Ticket: SKILLS-FRICTION-001
Status: active
Topics:
    - documentation
    - tooling
DocType: design-doc
Intent: long-term
Owners: []
RelatedFiles:
    - Path: abs:///home/manuel/code/wesen/go-go-golems/docmgr/ttmp/2026/09/10/DOCMGR-FRICTION-001--reduce-documentation-workflow-friction-with-deterministic-writes-and-coherent-milestones/design-doc/01-intern-guide-to-deterministic-document-mutation-and-milestone-workflows.md
      Note: Companion persistence and milestone design
    - Path: repo://diary/SKILL.md
      Note: Strict entry scope and relation rules
    - Path: repo://docmgr/SKILL.md
      Note: Ticket resume and relation guidance
    - Path: repo://remarkable-upload/SKILL.md
      Note: Specialist upload policy conflict
    - Path: repo://ticket-research-docmgr-remarkable/SKILL.md
      Note: Conflicting orchestration upload requirements
    - Path: repo://transcript-doc-friction-analysis/SKILL.md
      Note: Version-sensitive interpretation and implementation scope
    - Path: repo://ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/sources/session-evidence.json
      Note: Selected actual session records
ExternalSources: []
Summary: Session-grounded analysis and implementation plan for conflicting guidance, repeated context loading, diary overhead, evidence proportionality and trustworthy workflow evaluation.
LastUpdated: 2026-09-10T15:37:22Z
WhatFor: Teach an intern how this skills repository influences agent behavior and how to improve it without weakening user requirements or changing unrelated work.
WhenToUse: Before revising process skills, their references, validation helpers or resume conventions.
---


# Phase-aware skills and proportional evidence

## 1. What this ticket is trying to improve

A skill is a reusable instruction package, not executable policy enforcement. Its prose influences what an agent reads, which tools it calls, how it records progress and when it considers work complete. A skill can improve correctness while also creating unnecessary repeated work. The correct response is to make its obligations precise, not to remove validation indiscriminately.

This investigation examines the actual Video Observatory session `01a0837a-fb1c-7183-9bf5-26fce6d60551`, September 9–10, 2026. The session implemented a synthetic media lab, preserved four project reports and completed eight technical chapters. It also repeatedly reconciled documentation state, repaired generated whitespace and loaded overlapping instructions. The user explicitly requested detailed documentation and rigorous evidence; that legitimate scope must remain separate from avoidable administrative effort.

The strongest findings are specific:

- Two simultaneously loaded skills prescribe incompatible reMarkable workflows.
- The diary skill applies a large mandatory schema and broad relation rule to small milestones, while another skill recommends keeping relation lists small.
- The session repeatedly loaded broad process skills; its artifact graph duplicated current-state facts across several documents.
- The agent over-applied evidence preservation to a successful doctor log and initially inspected only the first diagram per chapter.
- The analysis skills themselves contain version-sensitive and overly categorical guidance that can misclassify behavior in this very session.

**Companion ticket:** `DOCMGR-FRICTION-001` in `/home/manuel/code/wesen/go-go-golems/docmgr`, under `ttmp/2026/09/10/`. Run `docmgr ticket show DOCMGR-FRICTION-001` there; this document's RelatedFiles metadata links its exact guide. Its guide owns stable serialization, recoverable close operations, future milestone APIs and resume data. This ticket owns how agents consume those capabilities. Do not teach proposed docmgr commands as if they already exist.

## 2. How this repository is used

The repository root is `/home/manuel/.pi/agent/skills`. Its inspected HEAD was `a6d2f00958837ec657542bc988721e1891252d6a`. Two go-minitrace skill files and several unrelated files were already modified/untracked. They are not part of this task and must not be staged, reset or overwritten. Current-file findings involving those files describe the inspected working tree, not necessarily the committed version or the version present throughout the earlier session.

The installed Pi package's `docs/skills.md` was read completely. The package is `@earendil-works/pi-coding-agent` in the Node v24.18.0 global installation on this machine. It documents discovery, frontmatter and progressive loading:

1. Pi discovers skill locations and includes names/descriptions in the prompt.
2. A matching task causes the agent to load `SKILL.md`, normally with `read`.
3. The skill can point to optional references, scripts and assets.
4. Relative references resolve from the skill directory.

`/skill:name` can explicitly load a skill. Standard skill metadata includes `name`, `description`, optional `compatibility`, `metadata` and `disable-model-invocation`. Unknown frontmatter fields are ignored by Pi. Therefore adding a custom `phase` field does not implement phase-aware loading by itself; that requires either prose conventions interpreted by the agent or an explicitly implemented extension.

![](/home/manuel/.pi/agent/skills/ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/sources/print/figure-1.png)

The session also had user-selected pinned skills whose full instructions remained in context. That is additional harness behavior, not the baseline progressive-disclosure model. Do not silently change the user's pins. A resume optimization must respect what is already present and which higher-priority instructions still require a read.

The new `ttmp/` workspace stores ticket documents, not new runtime skills. Its documents use docmgr frontmatter rather than skill `name`/`description`, and contain no `SKILL.md`. Keep research documents from accidentally becoming discoverable instruction packages.

### 2.1 Ownership boundaries

| Concern | Owner in this repository or elsewhere |
|---|---|
| Diary form and evidence level | `diary/SKILL.md` and `diary/references/diary.md` |
| Ticket commands and relation conventions | `docmgr/SKILL.md` |
| Research deliverable orchestration | `ticket-research-docmgr-remarkable/SKILL.md` and references |
| Upload mechanics and auth retry | `remarkable-upload/SKILL.md` |
| Textbook explanation quality | `textbook-authoring/SKILL.md` |
| Vault preservation and publication | `obsidian-vault-writing/SKILL.md` |
| Transcript discovery/fidelity | `go-minitrace-transcript-analysis/` |
| Friction heuristics and interpretation | `transcript-doc-friction-analysis/` |
| Mandatory session summaries, tool availability, some full-read rules | Higher-priority session/harness instructions, not necessarily files in this repo |
| Docmgr's actual persistence/API behavior | Companion docmgr repository/ticket |

A skill cannot override higher-priority user/developer instructions. When a root instruction mandates a particular read or evidence step, changing a lower-level skill alone cannot remove that obligation. Record the responsible owner instead of pretending a wording change fixes every layer.

## 3. Evidence method and its limitations

We copied the native session into a temporary snapshot without modifying the native store. `sources/native-session-list.txt`, `snapshot-source-list.txt` and `snapshot-sha256.txt` record provenance. Conversion output is in `sources/conversion.log`; the full normalized archive remains under `/tmp/doc-friction-session/archive`, outside Git. Selected query outputs and the query itself are retained in this ticket.

The five shipped docmetrics verbs were run: documentation consumption, source probes, API calls, failure triage and episodes. Their output is candidate evidence, not an automatic verdict. `scripts/01-session-evidence.sql` selects relevant tool records; those records were read and checked against actual source artifacts and commits.

### 3.1 Useful observations

Before normalized turn 1505, where this post-mortem discussion begins, the profile records:

| Skill file | Explicit read operations |
|---|---:|
| `diary/SKILL.md` | 6 |
| `docmgr/SKILL.md` | 5 |
| `textbook-authoring/SKILL.md` | 5 |
| `obsidian-vault-writing/SKILL.md` | 5 |
| `remarkable-upload/SKILL.md` | 3 |

These are reads, not five or six unique instruction versions, and not proof every reread was wasteful. They exclude implicit/pinned prompt inclusion. At turn 1440, four broad skills were read together; the tool records confirm the requests and returned text.

Normalized turns 1228, 1497 and 1499 contain actual Git blank-EOF diagnostics. The original Step 22 diary and source commit `ed265a5b049f882a15f97ddbabdefa2b94a413c4` corroborate the fixes and compressed doctor success log. The original script `04-render-textbook.cjs` initially captured only the first diagram; later changes captured all diagrams, and the final Chapter 2 secondary diagram was corrected at vault commit `67ef451b09cd124c1371c6964260fe80bbd67ae9`.

### 3.2 Corrections to automated interpretation

The profile reports zero ticket-document reads, although selected tool records and the session show ticket reads. Relative-path or argument-extraction classification needs investigation; zero is not evidence of non-use. It also reports no embedded-help calls despite help invocations visible in the session. These fields are not used to claim missing doc consumption.

The API-call heuristic emits many cache-collapse “compaction events,” while the snapshot contains **six actual native `compaction` records**. Cache drops are not an authoritative compaction counter. No precise “time wasted” percentage or dollar estimate is claimed here, and the session's whole token budget is not attributed to docmgr.

Failure triage labels include ordinary test failures, command batches and partially successful operations. Each candidate needs actual result inspection. For this ticket, the observed EOF failures and the upload-instruction conflict are stronger evidence than a global heuristic failure count.

## 4. Specific guidance that should change

### 4.1 A literal upload-policy conflict

`ticket-research-docmgr-remarkable/SKILL.md:127–164` requires a dry-run workflow containing `remarquee status`, `cloud account`, upload and a verification listing. `remarkable-upload/SKILL.md:8–20` says **never** run routine status/account checks and **never** list after a successful upload. Both texts were returned in the original session at normalized turn 4; this is not merely a conflict discovered in today's working tree.

The research reference `deliverable-checklist.md` repeats the preflight/account/listing requirements. Updating only one visible command block would leave the contradiction active elsewhere.

**Proposed fix:** the specialist upload skill owns mechanics and authentication. The orchestration skill states deliverable intent and delegates to that skill. An explicit user requirement for independent listing or dry-run remains binding; otherwise define a single success-evidence policy. Avoid both unconditional “always verify again” and unconditional “never verify” when the user explicitly requests stronger evidence.

A replacement policy sketch:

```text
For reMarkable delivery, follow remarkable-upload for commands and auth.
Preserve the upload result and destination.
Perform dry-run or independent listing when required by the user,
when preventing overwrite requires inspecting existing state,
or when upload results are ambiguous.
Do not add routine account/status calls solely because this is a ticket.
```

This is proposed wording, not an amendment applied during this research task. Until the owners resolve the conflict, the active higher-priority workflow controls this delivery; do not silently claim the contradictory instructions are already repaired.

### 4.2 Diary scope is too coarse

`diary/SKILL.md:65–133` defines a strict step format with many headings, prompt context and review/follow-up sections. Lines 39–62 show a recommended code-commit → task → diary/relations/changelog → docs-commit loop. The loop is **recommended**, not a command to create two commits for every tiny change; the agent over-applied it.

The rule to relate every modified or decision-shaping file is much broader than `docmgr/SKILL.md`'s guidance to keep related files roughly 3–7 and focus them on subdocuments. This is a scope tension, not a strict logical contradiction: one can distribute references among documents, but the resulting administrative work grows quickly.

The original session's Steps 20–22 included extensive publication narration and continuation/budget prompt text. Some of that follows the prompt-verbatim requirement; some came from the agent treating each milestone as a full investigation. The improvement should preserve original intent without repeating runtime counters.

**Proposed fix:** two explicit diary modes with the same evidence discipline:

```text
Milestone entry:
  outcome and reason
  evidence/commit references
  noteworthy failure or decision, if any
  remaining requirement IDs and next action

Investigation entry:
  full narrative, hypotheses, exact failures, decisions,
  tricky implementation details and review instructions
```

Use investigation mode for substantive debugging/design or an explicit user request. Use milestone mode for a clean publication, completed test batch or routine bookkeeping. Record the original user request once with a durable reference; distinguish authored instructions from automatically supplied runtime metadata. Never fabricate a verbatim prompt from a paraphrase or a reconstructed budget block.

### 4.3 Resume instructions repeat too much context

The original writing contract required reading the contract, TOC and selected brief when resuming. That was sensible for preventing scope loss across a large feature. The problem was adding broad skill reloads and repeated historical-status reconstruction on top of it without checking what remained applicable.

`docmgr/SKILL.md` says to read the diary before resuming. That should identify the latest relevant checkpoint, not imply reading a 1,000-line diary from the beginning on every turn. The session's general Pi-documentation instruction also required complete reads and following related Markdown links; its owner is outside this skill's local workflow. Do not blame `textbook-authoring` for a global read rule it did not define.

**Proposed fix:** a resume packet with current phase, requirement IDs, artifact revisions, unresolved questions, next action and pointers. Load stable full instructions at first use or when changed/absent; load only relevant references thereafter where higher-priority instructions permit it. A recorded hash is a change signal, not proof the model remembers the content.

### 4.4 Evidence preservation was not proportional

Preserving raw FFmpeg diagnostics alongside a readable normalized log protected meaningful experiment evidence. Applying the same pattern to a six-line successful doctor report produced unnecessary work. Neither a stronger raw archive nor another receipt made “All checks passed” more scientifically meaningful.

**Proposed fix:** define evidence classes. Routine success records command, exit/result and revision. A meaningful experiment additionally records configuration and interpreted measurements. Failure investigations retain exact diagnostic context where it matters. Exact-byte preservation remains appropriate when byte identity is itself the claim, as it was for original published media assets.

### 4.5 Validation had the wrong granularity

The session repeatedly ran the renderer across all existing chapters while adding one new chapter. Some integration checks were useful, but repeatedly inspecting unchanged material was not necessary. More importantly, the initial renderer only photographed the first diagram, so broad repeated checks still missed one secondary diagram's readability issue.

**Proposed fix:** check every changed diagram and affected dependency, then run one full final integration sweep. Preserve real visual inspection; syntax success alone is insufficient. `textbook-authoring/SKILL.md`'s foundational prose and no-analogy rules helped the output and should not be removed to reduce overhead.

### 4.6 The friction-analysis guidance has its own drift

`transcript-doc-friction-analysis/SKILL.md:96` describes Codex success as always 1, while the current base transcript skill documents nullable outcomes and newer fidelity behavior. The interpretation reference preserves older adapter observations. Version-scope those statements; do not turn an old empirical limitation into a universal rule.

The interpretation reference also says the delivery problem is “never content quality (so far)” based on earlier sessions. This session supplies a counterexample: conflicting content was actually loaded. Replace the categorical sentence with a dated finding and an explicit obligation to test content correctness.

“Deliverables are always changes” in the friction skill should not cause an agent to modify skills when the user asks only for an opinion. Gate implementation on the request. In this task, the user requested tickets and guides; production skill rewrites remain future work.

### 4.7 Other guidance needs a capability boundary

The docmgr repository's `AGENT.md` tells agents to run `format_file` at the end of each response. That tool is not exposed in this session. This is a current repository-guidance portability issue, not evidence that it caused the earlier textbook work. Recommend “use the repository formatter when available; otherwise name and run the documented equivalent,” without inventing a tool call.

Keep explicit source/tool ownership in the findings. Some improvements belong to harness configuration, some to docmgr and some to these skill files. One broad new skill cannot override all three layers safely.

## 5. Proposed phase-aware design

### 5.1 Minimal core with explicit escalation

Keep each process skill's always-loaded core short: purpose, triggers, non-negotiable safety rules, phase selection and reference map. Put detailed investigation templates, publication mechanics and API specifics in named references.

![](/home/manuel/.pi/agent/skills/ttmp/2026/09/10/SKILLS-FRICTION-001--make-skills-phase-aware-proportional-and-consistent-across-long-sessions/sources/print/figure-2.png)

Suggested local layout:

```text
diary/
  SKILL.md
  references/milestone-entry.md
  references/investigation-entry.md
  references/evidence-levels.md

ticket-research-docmgr-remarkable/
  SKILL.md
  references/phase-checklists.md
  references/resume-packet.md
  references/deliverable-checklist.md
```

These are proposed files. Do not add a second competing template without retiring or redirecting the old one. Existing detailed history should remain readable; new entries adopt the accepted convention prospectively.

### Decision: phase metadata is advisory until implemented

- **Context:** Pi ignores unknown frontmatter keys; the repository cannot create runtime behavior through YAML alone.
- **Options:** A harness extension, convention-only prose, or a helper that emits a resume packet.
- **Proposed decision:** Begin with prose and a small validator/helper; add runtime integration only after demonstrating value.
- **Rationale:** Most observed waste comes from contradictory and over-broad instructions, not a missing scheduler.
- **Consequences:** Evaluation must measure actual agent behavior, not merely whether `phase:` appears in a file.
- **Status:** proposed.

### 5.2 A compact checkpoint contract

```yaml
schema_version: 1
ticket: EXAMPLE-001
phase: validate
latest_milestone: chapter-08-reviewed
required_next:
  - final-contract-audit
verified:
  - artifact: outputs/presentation-demo.json
    revision: recorded-commit
    check: deterministic-output-match
instruction_refs:
  - path: diary/SKILL.md
    sha256: recorded-digest
open_questions: []
```

This is an illustrative schema, not an existing docmgr API. The companion ticket proposes generating it from canonical milestone records rather than copying the same facts into a new independent source of truth.

Resume pseudocode:

```text
read current request and applicable higher-priority instructions
load latest checkpoint and current artifact status
if checkpoint conflicts with files or current request: investigate the conflict
if instruction is absent or changed: load the relevant skill
load only references needed for the next unresolved requirement
execute that concrete action
record one evidence-backed milestone
```

A checkpoint must never authorize ignoring a new user instruction, assume an earlier goal is still active, or label a test pass as full contract completion.

## 6. Incremental validation and instruction checks

A small validation manifest can distinguish content edits from rendering-environment changes:

```text
key = hash(document bytes + referenced asset hashes
           + renderer version + stylesheet + validation policy)
if key differs: run targeted checks and inspect every affected figure
if shared renderer/policy changes: invalidate all dependent documents
at final delivery: verify the complete manifest and all requirements
```

The manifest tracks evidence, not a replacement for judgment. An unchanged hash does not prove an earlier review was competent; the first-diagram-only issue is why the policy version belongs in the key.

For skill consistency, begin with explicit checks rather than pretending free-form prose can be exhaustively linted:

- Validate name/description, local reference existence and relative-path resolution.
- Detect duplicate policy headings and known contradictory command requirements.
- Test composed workflow fixtures: research plus upload; diary plus docmgr; transcript analysis plus current adapter semantics.
- Flag instructions naming unavailable tools as capability-dependent.
- Keep semantic conflict findings reviewable; keyword matches are candidates, not automatic edits.

The research writing-style reference currently repeats a “Decision Records” section. Consolidating that duplication is a small, low-risk change; replacing all long references with summaries is not.

## 7. Implementation guide and acceptance tests

### Phase 0 — preserve state and establish evidence

Record Git status and inspect links before editing. The diary paths under `.pi` and `.claude` resolve to the same inode on this machine; that establishes shared underlying file identity, not necessarily the precise link topology. Check directory symlinks and hardlinks before choosing a write strategy. Never accidentally break a shared mirror by write-via-rename.

Run the retained query against the frozen archive if still available, or reconvert a newly fingerprinted snapshot. Do not compare a growing session to an earlier snapshot without stating the new cutoff. Read `sources/session-evidence.json` before interpreting aggregate profiles.

Acceptance: every proposed fix has a concrete instruction/source/evidence reference and an owner. No fabricated time savings, no unexplained edits to pre-existing work.

### Phase 1 — resolve policy conflicts

Edit research and upload instructions together, including their checklists. Decide who owns success verification and when user-required dry-run/listing overrides the default. Fix the stale adapter claims and duplicate writing-style decision section. Submit focused diffs rather than changing all skills at once.

Acceptance fixtures: normal successful upload; explicit independent verification request; ambiguous failure; authentication retry; overwrite risk. Each composed instruction set must prescribe a coherent path and preserve the user's requirements.

### Phase 2 — introduce diary modes and resume guidance

Define milestone versus investigation escalation criteria. Preserve the exact-request rule once, with references thereafter. Clarify relation scope: primary implementation/evidence files in metadata, complete changed-path lists in a receipt when needed. Avoid generating separate narrative updates for every projection of one milestone.

Acceptance fixtures: clean documentation publish; multi-step debugging with two failures; compaction after a verified milestone; changed source after checkpoint; user asks only for analysis. The agent should neither omit real failure context nor fabricate a full investigation for routine success.

### Phase 3 — add helpers and dependency-aware checks

Build a small reference/link/policy fixture checker and optional checkpoint validator. If the docmgr milestone/resume interface is not implemented yet, use existing commands and label the future integration. Do not install invented command names in an active skill.

Acceptance: broken references fail; known upload-policy contradictions fail; unchanged dependencies avoid repeated rendering; changed renderer policy invalidates all affected results; every changed diagram is inspected.

### Phase 4 — re-measure without gaming the outcome

Run comparable future sessions with the same task class and evidence requirements. Compare redundant full-skill reloads, number of independently maintained current-state records, unnecessary mutation diffs and validation coverage. Also track missed requirements, unsupported success claims and lost failure context.

A lower tool-call count is not success if the agent stops checking actual media, suppresses errors or skips publication verification. Do not use the entire historical session's elapsed time as a controlled baseline. The claim to validate is narrower: less avoidable administrative work for the same verified outcome.

## 8. Review plan and open decisions

The first review should involve the owners of the diary, research and upload workflows together. Approving a specialist change while leaving its orchestrator contradictory recreates the problem. A second review should cover transcript adapter/version semantics and any harness-level rules outside this repository.

Open decisions include whether a compact checkpoint should be YAML or generated JSON, whether any runtime integration is worthwhile, and which publication checks are defaults versus explicit user obligations. These decisions do not block the immediate correction of literal conflicts and byte-level docmgr bugs.

This ticket delivers analysis and an intern-ready implementation plan. It does not change production skills. Related implementation tasks remain open after the research documents and reMarkable delivery are complete.

## 9. Evidence and API references

- `sources/session-evidence.json`: selected actual tool records, including original conflicting skill loads and EOF errors.
- `scripts/01-session-evidence.sql`: reproducible normalized query.
- `sources/doc-consumption.json`, `api-calls.json`, `failure-triage.json`, `episodes.json`, `source-probes.json`: heuristic profiles, interpreted with the corrections above.
- `sources/native-session-list.txt`, `snapshot-source-list.txt`, `snapshot-sha256.txt`, `conversion.log`: snapshot provenance.
- `sources/guidance-map.txt`: line references for the inspected skill instructions.
- Original project ticket's `reference/01-investigation-diary.md`, Steps 20–22, and `sources/textbook-final-contract-audit.md`: external artifact corroboration.
- Installed Pi `docs/skills.md`: actual discovery/frontmatter/loading semantics; no unimplemented phase metadata is attributed to Pi.
- Companion docmgr guide and reproducers: newline growth, changelog EOF and partial-close evidence; proposed future milestone/resume contracts.
