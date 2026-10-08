# daitai Project Status

This document describes the current design direction and open considerations for `daitai`. Past changes are recorded in the [CHANGELOG](CHANGELOG.md).

## Development stage

daitai is at an early stage. Its reading convention, the readings provided through `da.*`, and examples will be revised through actual use.

## Scope

daitai is a domain-free **reading convention** for how an LLM should interpret structured YAML.

It does not assume in advance what a description is about. The domain is inferred from key names, hierarchy, natural-language scalars, and surrounding context.

## Documentation center

The reader is an LLM, and no dedicated parser or validator is assumed. Ordinary YAML structure and natural language are read together, with meaning inferred from names and context rather than encoded through a fixed type system.

[HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) is the core document. The reading convention and the readings provided through `da.*` are kept together there.

## Readings provided through `da.`

The `da.` prefix indicates that daitai provides a reading for that entry.

A reading may cover the whole name, as in `da.intent`, or only part of it, as in `da.group.*`. In the latter case, the remaining name is interpreted as ordinary language from context.

A new provided reading is useful when ordinary YAML and natural language leave an important relationship easy to misread and there is value in sharing that reading in advance.

## Examples

The documentation uses examples such as a photo-organizing application because they are close to current use cases. The domain of an example does not limit the scope of the reading convention.
