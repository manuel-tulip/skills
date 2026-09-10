---
title: "Investigation diary"
Title: Investigation diary
Ticket: SKILLS-FRICTION-001
Status: active
Topics: [documentation, tooling]
DocType: reference
Intent: long-term
Owners: []
RelatedFiles: []
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

The profile reports zero ticket reads/help consumption despite inspected counterexamples, and cache-collapse candidates are not a reliable compaction count. Those fields are retained as heuristic output but excluded from causal claims. The repository had no `ttmp` workspace initially; initialization was expected setup, not a product failure.

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

Original session: `01a0837a-fb1c-7183-9bf5-26fce6d60551`. Full archives remain outside Git under `/tmp/doc-friction-session`; selected evidence and provenance are committed with the ticket. The active pinned research workflow and specialist upload skill still conflict; this task documents that conflict rather than silently changing the policy.
