#!/usr/bin/env python3
"""work_slip.py — generate and print brutalist thermal work slips.

Two modes (the constrained DSL):

  status  Progress slip for current work: task id, title, summary, what was
          done, what was tricky (optional), what's next, optional QR code
          linking to a commit URL on GitHub.

  plan    Up-front slip listing the full task phases as a checklist, with an
          optional QR code linking to an arbitrary URL (ticket, PR, docs).

Both modes emit an almanach layout YAML and (unless --no-print) print it via
`almanach-render-service print-remote`.

Examples:
  work_slip.py status --task GEPPETTO-RERANKER-002 --label "STEP 3" \
      --title "Wired In: Factory, JS, Docs" \
      --summary "Factory + validation wired, JS parity proven." \
      --did "factory cohere case" --did "goja parity test" \
      --tricky "base-url override placement" \
      --next "P6 final validation" \
      --commit 66b4e650 --repo go-go-golems/geppetto

  work_slip.py plan --task GEPPETTO-RERANKER-002 --label PLAN \
      --title "Cohere Rerank Salvage Plan" \
      --summary "Port PR #169 onto pkg/rerank, drop legacy API." \
      --phase "P1 adapter core" --phase "P2 mock-server tests" \
      --phase "P3 factory wiring" --phase "P4 goja parity" \
      --phase "P5 docs + live test" --phase "P6 validation" \
      --next "P1 adapter core" \
      --url https://github.com/go-go-golems/geppetto/pull/169
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile

import yaml

PRINTER_CMD = os.environ.get("ALMANACH_CMD", "almanach-render-service")


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def die(msg: str) -> "None":
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def warn(msg: str) -> None:
    print(f"warning: {msg}", file=sys.stderr)


def detect_repo() -> str | None:
    """Derive 'owner/name' from the git origin remote of the cwd, if any."""
    try:
        url = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return f"{m.group(1)}/{m.group(2)}" if m else None


def commit_url(commit: str, repo: str | None) -> str | None:
    if not commit:
        return None
    if not repo:
        repo = detect_repo()
    if not repo:
        warn("--commit given but no --repo and no git origin detected; QR omitted")
        return None
    return f"https://github.com/{repo}/commit/{commit}"


def check_title(title: str) -> None:
    # At 384 dots an h1 line fits ~2-3 words / ~18 chars.
    if len(title) > 54:
        warn(f"title is {len(title)} chars; h1 fits ~3 short lines (~54 chars max)")


def base_layout() -> dict:
    return {
        "almanach_studio_version": 1,
        "theme": "brutalist",
        "paperWidth": 384,
        "bodyScale": 1,
        "feedLines": 8,
        "blocks": [],
    }


def header_blocks(blocks: list, task: str, label: str) -> None:
    blocks.append({
        "id": "head", "type": "row",
        "data": {"cols": [
            {"w": "1fr", "text": task, "preset": "micro"},
            {"w": "1fr", "text": label, "preset": "micro", "align": "right"},
        ]},
    })
    blocks.append({"id": "r1", "type": "rule", "data": {"weight": "heavy"}})
    blocks.append({"id": "gap1", "type": "space", "data": {"size": "s"}})


def title_summary_blocks(blocks: list, title: str, summary: str | None) -> None:
    check_title(title)
    blocks.append({
        "id": "title", "type": "text",
        "data": {"text": title, "preset": "h1", "lines": 3},
    })
    if summary:
        blocks.append({"id": "gap2", "type": "space", "data": {"size": "s"}})
        blocks.append({
            "id": "summary", "type": "text",
            "data": {"text": summary, "preset": "body"},
        })


def qr_block(blocks: list, caption: str, url: str) -> None:
    blocks.append({
        "id": "decide", "type": "row",
        "data": {"cols": [
            {"w": "1fr", "text": caption, "preset": "caption"},
            {"w": 120, "blocks": [
                {"id": "qr", "type": "qr", "data": {"value": url, "size": 110}},
            ]},
        ]},
    })


# ---------------------------------------------------------------------------
# mode: status
# ---------------------------------------------------------------------------

def build_status(args: argparse.Namespace) -> dict:
    if not args.did:
        die("status mode requires at least one --did item")
    if not args.next:
        die("status mode requires --next")

    layout = base_layout()
    b = layout["blocks"]
    header_blocks(b, args.task, args.label)
    title_summary_blocks(b, args.title, args.summary)

    b.append({"id": "gap3", "type": "space", "data": {"size": "m"}})
    b.append({
        "id": "did", "type": "list",
        "data": {"marker": "—", "lines": 2, "items": args.did},
    })
    if args.tricky:
        b.append({"id": "gap4", "type": "space", "data": {"size": "s"}})
        b.append({
            "id": "tricky", "type": "list",
            "data": {"marker": "!", "lines": 2, "items": args.tricky},
        })

    b.append({"id": "r2", "type": "rule", "data": {"weight": "hair"}})
    facts = []
    if args.commit:
        facts.append(["COMMIT", args.commit])
    facts.append(["NEXT", args.next])
    for kv in args.fact or []:
        if "=" not in kv:
            die(f"--fact must be KEY=VALUE, got {kv!r}")
        k, v = kv.split("=", 1)
        facts.append([k, v])
    b.append({"id": "facts", "type": "kv", "data": {"items": facts}})

    url = commit_url(args.commit, args.repo)
    if url:
        b.append({"id": "r3", "type": "rule", "data": {"weight": "hair"}})
        qr_block(b, "SCAN FOR COMMIT", url)
    return layout


# ---------------------------------------------------------------------------
# mode: plan
# ---------------------------------------------------------------------------

def build_plan(args: argparse.Namespace) -> dict:
    if not args.phase:
        die("plan mode requires at least one --phase item")

    layout = base_layout()
    b = layout["blocks"]
    header_blocks(b, args.task, args.label)
    title_summary_blocks(b, args.title, args.summary)

    b.append({"id": "gap3", "type": "space", "data": {"size": "m"}})
    b.append({
        "id": "planhead", "type": "text",
        "data": {"text": "PLAN", "preset": "h2"},
    })
    b.append({
        "id": "plan", "type": "checks",
        "data": {"items": args.phase},
    })

    b.append({"id": "r2", "type": "rule", "data": {"weight": "hair"}})
    facts = [["PHASES", str(len(args.phase))]]
    if args.next:
        facts.append(["NEXT", args.next])
    for kv in args.fact or []:
        if "=" not in kv:
            die(f"--fact must be KEY=VALUE, got {kv!r}")
        k, v = kv.split("=", 1)
        facts.append([k, v])
    b.append({"id": "facts", "type": "kv", "data": {"items": facts}})

    if args.url:
        b.append({"id": "r3", "type": "rule", "data": {"weight": "hair"}})
        qr_block(b, "SCAN FOR REF", args.url)
    return layout


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate and print brutalist thermal work slips.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = ap.add_subparsers(dest="mode", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--task", required=True, help="Task/ticket id, e.g. GEPPETTO-RERANKER-002")
    common.add_argument("--label", default="STATUS",
                        help="Top-right label, e.g. 'STEP 3' or 'PLAN' (default: STATUS)")
    common.add_argument("--title", required=True, help="h1 headline (~3 short lines max)")
    common.add_argument("--summary", default=None, help="One short body paragraph (optional)")
    common.add_argument("--next", default=None, help="What's next (short)")
    common.add_argument("--fact", action="append", default=[],
                        help="Extra KEY=VALUE fact row (repeatable)")
    common.add_argument("--out", default=None,
                        help="Write layout YAML here (default: temp file)")
    common.add_argument("--no-print", action="store_true",
                        help="Only generate the YAML; do not print")
    common.add_argument("--dry-run-remote", action="store_true",
                        help="Render remotely without printing (validates layout)")

    p_status = sub.add_parser("status", parents=[common],
                              help="Progress slip for current work")
    p_status.add_argument("--did", action="append", default=[],
                          help="One 'what was done' bullet (repeatable, required)")
    p_status.add_argument("--tricky", action="append", default=[],
                          help="One 'what was tricky' bullet (repeatable, optional)")
    p_status.add_argument("--commit", default=None,
                          help="Commit hash; QR links to the GitHub commit URL")
    p_status.add_argument("--repo", default=None,
                          help="owner/name for the commit URL (default: git origin)")

    p_plan = sub.add_parser("plan", parents=[common],
                            help="Up-front slip listing all task phases")
    p_plan.add_argument("--phase", action="append", default=[],
                        help="One phase line (repeatable, required), e.g. 'P1 adapter core'")
    p_plan.add_argument("--url", default=None,
                        help="URL for the QR code (ticket, PR, docs)")

    args = ap.parse_args()
    layout = build_status(args) if args.mode == "status" else build_plan(args)

    out = args.out
    if not out:
        fd, out = tempfile.mkstemp(prefix="work-slip-", suffix=".yaml")
        os.close(fd)
    with open(out, "w") as f:
        yaml.safe_dump(layout, f, sort_keys=False, allow_unicode=True, width=120)
    print(f"layout: {out}")

    if args.no_print:
        return

    cmd = [PRINTER_CMD, "print-remote", "--layout", out, "--output", "yaml"]
    if args.dry_run_remote:
        cmd.append("--dry-run")
    result = subprocess.run(cmd, capture_output=True, text=True)
    sys.stdout.write(result.stdout)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        die(f"print command failed (exit {result.returncode})")
    if result.stdout.count("ok: true") < 1:
        sys.stderr.write(result.stderr)
        die("print did not report ok: true")
    print("printed: " + ("no (dry run)" if args.dry_run_remote else "yes"))


if __name__ == "__main__":
    main()
