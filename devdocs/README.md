# devdocs/

`devdocs/` is the workspace for managing the documents in this repository with [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc).

## Layout

```text
devdocs/
├── canonical_sources/    canonical sources (Python)
│   ├── readme/
│   ├── status/
│   ├── changelog/
│   ├── guides/           HOW_TO_READ_DAITAI
│   └── workspace/        this README
├── config/
│   └── notice.toml       notice and publication policy embedded at the top of generated documents
└── canonical_documents/  Japanese documents generated from the canonical sources
```

- The Python in `canonical_sources/` is the canonical source of the documents. Edit it when changing a document.
- `canonical_documents/` is generated output. It is kept in Git for review but is not edited directly.
- The repository-root `README.md`, `HOW_TO_READ_DAITAI.md`, `STATUS.md`, and `CHANGELOG.md`, together with this `devdocs/README.md`, are published English translations of `canonical_documents/`.

## Generation

From anywhere in the repository, regenerate `canonical_documents/` with:

```bash
python scripts/render_docs.py
```

Because the `shikumi-devdoc` CLI does not add the current directory to the import path, this script adds the repository root to `PYTHONPATH` and invokes the CLI.

## Published documents

Published versions are created by an LLM translating the Japanese canonical documents into English. The translation policy is stored in `config/notice.toml` and embedded as a comment at the top of generated documents. That comment is not included in the published versions.

When a canonical source changes, regenerate the canonical document and update the corresponding published translation as well.

## Checks

Install the development dependencies and run:

```bash
python -m pip install -r requirements-dev.txt
ruff format --check .
ruff check .
basedpyright
pytest
```

The tests check that canonical documents are in sync with their sources, that YAML examples are ordinary valid YAML without duplicate keys in a mapping, and that all published versions exist. They do not validate the semantic correctness of daitai.

GitHub Actions (`.github/workflows/checks.yml`) runs the same checks with Python 3.11 on every push to `main` and every pull request. CI does not check whether published translations are up to date with the canonical documents.
