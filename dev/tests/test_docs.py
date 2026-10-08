"""Checks for the documentation of daitai.

daitai itself has no parser or validator, and these tests do not add one. They
only check that

- the committed canonical documents are in sync with their canonical sources,
- every published document exists and carries no generation notice, and
- every ``yaml`` example in the documents is plain, well-formed YAML without
  duplicate keys in a single mapping.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

DEV_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = DEV_ROOT.parent
CANONICAL_ROOT = DEV_ROOT / "devdocs" / "canonical_documents"

sys.path.insert(0, str(DEV_ROOT / "scripts"))
import render_docs  # pyright: ignore[reportMissingImports]

# canonical document (relative to CANONICAL_ROOT) -> published document
# (relative to REPO_ROOT)
PUBLISHED: dict[str, str] = {
    "README.md": "README.md",
    "STATUS.md": "dev/STATUS.md",
    "CHANGELOG.md": "dev/CHANGELOG.md",
    "HOW_TO_READ_DAITAI.md": "HOW_TO_READ_DAITAI.md",
    "devdocs/README.md": "dev/devdocs/README.md",
}

YAML_FENCE = re.compile(
    r"^(?P<indent>[ \t]*)```yaml\n(?P<body>.*?)^(?P=indent)```",
    re.MULTILINE | re.DOTALL,
)


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate keys within one mapping."""


def _construct_mapping(
    loader: yaml.SafeLoader, node: yaml.MappingNode
) -> dict[Any, Any]:
    seen: set[Any] = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node)  # pyright: ignore[reportUnknownMemberType]
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        seen.add(key)
    return loader.construct_mapping(node)


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping
)


def _all_documents() -> list[Path]:
    canonical = [CANONICAL_ROOT / name for name in PUBLISHED]
    published = [REPO_ROOT / name for name in PUBLISHED.values()]
    return canonical + published


def _yaml_examples(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    examples: list[tuple[int, str]] = []
    for match in YAML_FENCE.finditer(text):
        indent = match.group("indent")
        lines = match.group("body").splitlines()
        body = "\n".join(line.removeprefix(indent) for line in lines)
        line_number = text.count("\n", 0, match.start()) + 1
        examples.append((line_number, body))
    return examples


def test_canonical_documents_are_in_sync(tmp_path: Path) -> None:
    render_docs.render(tmp_path)
    for name in PUBLISHED:
        expected = (tmp_path / name).read_text(encoding="utf-8")
        actual = (CANONICAL_ROOT / name).read_text(encoding="utf-8")
        assert actual == expected, (
            f"{name} is out of date; run `python dev/scripts/render_docs.py`"
        )


@pytest.mark.parametrize("published", sorted(PUBLISHED.values()))
def test_published_document_exists_without_notice(published: str) -> None:
    path = REPO_ROOT / published
    assert path.is_file(), f"published document {published} is missing"
    text = path.read_text(encoding="utf-8")
    assert "shikumi-devdoc` によって生成された" not in text
    assert not text.lstrip().startswith("<!--")


@pytest.mark.parametrize(
    "path", _all_documents(), ids=lambda p: str(p.relative_to(REPO_ROOT))
)
def test_yaml_examples_are_well_formed(path: Path) -> None:
    if not path.is_file():
        pytest.skip(f"{path.relative_to(REPO_ROOT)} does not exist")
    for line_number, body in _yaml_examples(path):
        try:
            list(yaml.load_all(body, Loader=_UniqueKeyLoader))
        except yaml.YAMLError as error:
            pytest.fail(f"{path.relative_to(REPO_ROOT)}:{line_number}: {error}")
