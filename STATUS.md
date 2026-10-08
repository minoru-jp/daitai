# daitai Project Status

This document describes the current design direction and open considerations for `daitai`. Past changes are recorded in the [CHANGELOG](CHANGELOG.md).

## Development stage

daitai is at an early stage. Its reading convention, the readings provided through `da.*`, and examples will be revised through actual use.

## Purpose

daitai is a **reading convention for conveying intent and structure to LLMs through YAML**. It uses ordinary YAML and does not require a formal schema.

## Filename identification

`*.daitai.yml` and `*.daitai.yaml` are the filename forms for YAML documents to which the daitai reading convention applies. Ordinary `*.yml` and `*.yaml` files should not be assumed to use daitai based on their filenames alone.

`.daitai` does not introduce another format. It is a filename marker indicating that the YAML document is to be read using the daitai reading convention.

## Documentation center

The reader is an LLM, and no dedicated parser or validator is assumed. Ordinary YAML structure and natural language are read together, with meaning inferred from names and context rather than encoded through a fixed type system.

[HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) is the core document. The reading convention and the readings provided through `da.*` are kept together there.

## Readings provided through `da.`

The `da.` prefix indicates that daitai provides a reading for that entry.

A reading may cover the whole name, as in `da.intent`, or only part of it, as in `da.group.*`. In the latter case, the remaining name is interpreted as ordinary language from context.

A new provided reading is useful when ordinary YAML and natural language leave an important relationship easy to misread and there is value in sharing that reading in advance.

## Examples

The documentation uses examples such as a photo-organizing application because they are close to current use cases.
