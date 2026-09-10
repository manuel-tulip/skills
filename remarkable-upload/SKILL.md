---
name: remarkable-upload
description: Upload Markdown and source files to a reMarkable device as PDFs using the remarquee CLI (rmapi-backed). Use when the user asks to upload/send/export docs/examples to reMarkable, bundle multiple files into one PDF with a ToC, choose an /ai/YYYY/MM/DD destination, avoid or force overwrites, or troubleshoot pandoc/xelatex/rmapi auth.
---

# Remarkable Upload

## Delivery policy owner

This specialist skill owns upload mechanics, authentication and success evidence. Research orchestrators delegate here rather than duplicating commands. Explicit user or higher-priority requirements override these defaults.

- A normal successful upload needs no routine status/account preflight or post-upload listing. Retain its `OK: uploaded` result and destination; this proves cloud delivery, not physical device synchronization.
- Run dry-run or independent listing when explicitly required, when an ambiguous result needs investigation, or when inspecting existing state is necessary to prevent overwrite. Dry-run describes the command; it does not render a PDF.
- Never use `--force` without authorization to replace the existing document and lose its annotations. Inspect or choose a new name when overwrite risk is unresolved.
- Let built-in 401/403 reauthentication finish. If it fails, one explicit `--reauth` attempt is reasonable; persistent auth failure is a blocker, not an invitation to loop.
- Use the reference below normally; inspect installed help when flags or behavior demonstrably differ. Do not repeatedly reload unchanged help out of habit.

## Typical workflow

**Normal upload:**
```bash
remarquee upload bundle <path...> --name "<doc name>" --remote-dir "/ai/YYYY/MM/DD/<folder>" --toc-depth 2 --non-interactive 2>&1
```

A clear successful result is sufficient by default. Perform any explicitly required independent verification before declaring delivery complete.

**If upload fails with auth error despite auto-retry** (the `NOTE: auth expired` message appears but the retry also fails):
```bash
remarquee upload bundle <path...> --name "<doc name>" --remote-dir "/ai/YYYY/MM/DD/<folder>" --toc-depth 2 --reauth --non-interactive 2>&1
```

This is rare — the auto-retry handles normal token expiry. Only use `--reauth` manually if the auto-retry also fails.

**If you need to check what's already on the device (e.g. to decide --force):**
```bash
remarquee cloud ls /ai/YYYY/MM/DD/<folder> --long --non-interactive 2>&1
```

Use this for needed state inspection or explicitly required verification, not as an automatic extra step.

## Command reference

### Upload commands

| Command | When to use | Key flags |
|---|---|---|
| `remarquee upload bundle` | Multiple .md files → one PDF with ToC | `--name`, `--remote-dir`, `--toc-depth`, `--force`, `--date`, `--non-interactive`, `--reauth`, `--dry-run` |
| `remarquee upload md` | Single or multiple .md files → separate PDFs | `--name`, `--remote-dir`, `--force`, `--date`, `--non-interactive`, `--reauth`, `--dry-run`, `--flatten` |
| `remarquee upload src` | Source code files → syntax-highlighted PDFs | `--name`, `--remote-dir`, `--force`, `--date`, `--non-interactive`, `--reauth`, `--dry-run`, `--bundle`, `--include-ext` |

### Common flags

- `--name "<title>"` — Document name (use simple names: no special chars, no colons, no parens). The PDF filename is auto-sanitized.
- `--remote-dir "/ai/YYYY/MM/DD/<folder>"` — Full remote path override
- `--date YYYY/MM/DD` — Sets date portion of remote path (default: today)
- `--force` — Overwrite existing document (WARNING: deletes existing + annotations)
- `--non-interactive` — Required for agent sessions (don't prompt for codes)
- `--reauth` — Force re-authentication when tokens are stale
- `--dry-run` — Preview what would happen without running pandoc or uploading
- `--toc-depth N` — ToC depth for bundle (default: 1)

### Cloud commands

| Command | When to use | Key flags |
|---|---|---|
| `remarquee cloud ls <path>` | List files on device | `--long`, `--non-interactive` |
| `remarquee cloud account` | Check auth status | `--non-interactive`, `--reauth` |
| `remarquee cloud get <path>` | Download a document | `--out-dir`, `--non-interactive` |
| `remarquee cloud search <query>` | Search by name | `--match name`, `--limit`, `--compact`, `--non-interactive` |
| `remarquee cloud rm <path>` | Delete a document | `--non-interactive` |

## Destination conventions

- Default remote directory: `/ai/YYYY/MM/DD/`
- Ticket-aware: `/ai/YYYY/MM/DD/<TICKET-ID>/`
- Always use `--non-interactive` in agent sessions

## Name sanitization

The CLI automatically sanitizes document names for upload:
- Spaces → underscores in PDF filenames
- Special characters that break rmapi are stripped

So you can use `--name "GOJA-053 FS Module Guide"` and the CLI will handle it.

## Common issues

- **Pandoc "Unknown alias" errors**: Usually caused by malformed code block syntax. Test with `pandoc <file>.md -o /tmp/test.pdf --pdf-engine=xelatex` to isolate.
- **Nested code blocks in markdown**: Use explicit language tags like ` ```markdown ` and ` ```json `. Do NOT use sed to replace all ` ``` ` markers.
- **401 Unauthorized during upload**: Wait for built-in retry first; if it fails, apply the bounded reauth policy above.
- **400 Bad Request during upload**: Usually a filename issue — use `--name` with a simple name (alphanumeric + spaces + dashes only).
