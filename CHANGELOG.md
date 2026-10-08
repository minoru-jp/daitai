# daitai Change Log

Changes to `daitai` are recorded by date.

## 2026-10-08

Created the initial daitai documentation set.

Added:

- Defined daitai as a domain-free reading convention for structured YAML interpreted by an LLM.
- Added the core LLM-facing document `HOW_TO_READ_DAITAI.md`, bringing together the reading convention and the readings provided through `da.*`.
- Defined `da.` as the prefix indicating that daitai provides a reading for an entry.
- Added initial provided readings for intent, important constraints, order, conditions, causality, references, reuse, group properties, and semantic boundaries.
- Added canonical document management with shikumi-devdoc, the document generation script, and CI running ruff, basedpyright, and pytest.

Changed:

- Defined `*.daitai.yml` and `*.daitai.yaml` as the filename forms for YAML documents to which the daitai reading convention applies.
- Clarified that ordinary `*.yml` and `*.yaml` files should not be assumed to use the daitai reading convention based on their filenames alone.
- Updated the description of daitai to focus on its purpose as a reading convention for conveying intent and structure to LLMs through YAML.
- Clarified that every provided `da.*` reading can be refined with additional names and interpreted across multiple value and structure patterns from context.
