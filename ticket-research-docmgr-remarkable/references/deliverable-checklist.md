# Deliverable Checklist

Use this checklist before final handoff.

## Ticket setup

- `docmgr ticket create-ticket` completed (or existing ticket confirmed)
- design doc exists
- diary doc exists
- index/tasks/changelog are updated

## Analysis quality

- architecture mapping is evidence-backed
- key claims reference files
- proposed solution includes APIs and pseudocode
- implementation plan is phased and actionable
- testing strategy is explicit

## Bookkeeping

- key files related via `docmgr doc relate`
- changelog updated with meaningful entries
- tasks reflect completion state

## Validation

- `docmgr doctor --ticket <TICKET-ID> --stale-after 30` passes
- vocabulary warnings resolved or intentionally accepted

## reMarkable delivery

- delivery was requested; otherwise this section is not applicable
- specialist `remarkable-upload` policy followed (no duplicated preflight/auth recipe)
- requested bundle uploaded, with successful result and destination retained
- dry-run, independent listing or state inspection performed when explicitly required or needed under that policy
- no unauthorized overwrite/annotation loss; ambiguous outcomes are not reported as success

## Final response

- include ticket path
- include doc paths
- include validation status
- include requested upload destination and the actual evidence level (upload result versus independent listing)
- include any open questions or residual risks

