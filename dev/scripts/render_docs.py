"""Regenerate the canonical documents under ``dev/devdocs/canonical_documents/``.

From the repository root::

    python dev/scripts/render_docs.py

``--output`` renders into another directory instead, which the tests use to
check that the committed canonical documents are in sync with their sources.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

DEV_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = DEV_ROOT.parent
NOTICE = DEV_ROOT / "devdocs" / "config" / "notice.toml"
DEFAULT_OUTPUT = DEV_ROOT / "devdocs" / "canonical_documents"

# (canonical source module or package, output directory relative to the root)
TARGETS: tuple[tuple[str, str], ...] = (
    ("dev.devdocs.canonical_sources.readme.canonical", "."),
    ("dev.devdocs.canonical_sources.status.canonical", "."),
    ("dev.devdocs.canonical_sources.changelog.canonical", "."),
    ("dev.devdocs.canonical_sources.guides", "."),
    ("dev.devdocs.canonical_sources.workspace.canonical", "devdocs"),
)


def _find_cli() -> list[str]:
    executable = shutil.which("shikumi-devdoc")
    if executable is not None:
        return [executable]
    return [sys.executable, "-m", "shikumi_devdoc.cli"]


def render(output_root: Path) -> list[Path]:
    """Render every canonical document into ``output_root``."""
    env = dict(os.environ)
    # The CLI imports canonical sources by dotted name; it does not add the
    # current directory to the import path by itself.
    env["PYTHONPATH"] = os.pathsep.join(
        [str(REPO_ROOT), *filter(None, [env.get("PYTHONPATH")])]
    )
    cli = _find_cli()
    written: list[Path] = []
    for module, relative_dir in TARGETS:
        out_dir = output_root / relative_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [
                *cli,
                "render",
                "document",
                module,
                "-o",
                str(out_dir),
                "--notice",
                str(NOTICE),
            ],
            cwd=REPO_ROOT,
            env=env,
            check=True,
            capture_output=True,
            text=True,
        )
        stdout: str = result.stdout or ""
        written.extend(Path(line) for line in stdout.splitlines() if line)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate the canonical documents.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="output root (default: dev/devdocs/canonical_documents)",
    )
    args = parser.parse_args()
    output: Path = args.output
    for path in render(output.resolve()):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
