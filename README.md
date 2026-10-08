# daitai

**daitai** is a domain-free **reading convention** for sharing how an LLM should interpret structured YAML descriptions.

Writers use ordinary YAML freely, expressing what they want to communicate through names, hierarchy, and natural-language scalars. Give [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) to the LLM so it can interpret the description using the shared reading convention.

## Basics

```yaml
about_gui_design:
  main_window:
    sidebar: On the left. Albums and tags
    photo_grid: In the center. Shows photos as thumbnails

import_pipeline:
  da.trigger: The user selects a folder and starts importing
  da.outcome: Register the photos in the library
```

`about_gui_design` and `main_window` are not fixed type names. The LLM reads key names, indentation-based structure, scalars, and surrounding context together.

The `da.` prefix indicates that daitai provides a reading for that entry. See [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md) when you want to use readings provided through `da.*`.

## Usage

1. Write what you want to communicate in ordinary YAML.
2. Give the LLM [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) together with the YAML.
3. When useful, use readings from `da.*` with [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md) as a quick reference.

daitai assumes no particular domain. What the description is about is inferred from the names, structure, and natural-language text actually present.

## Documentation

- [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md): The core of daitai. This is the reading convention intended for the LLM.
- [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md): Quick reference for the readings provided by daitai and for `da.*`.
- [Project Status](STATUS.md): Current design direction and open considerations.
- [CHANGELOG](CHANGELOG.md): Change history for daitai.

The documents are managed with [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc). Their canonical sources are under `devdocs/` (see [devdocs/README.md](devdocs/README.md)).

## License

daitai is released under the MIT No Attribution license (MIT-0). See [`LICENSE`](LICENSE).

You do not need to retain a copyright notice or permission notice. The reading guide and other documents may be freely copied and modified without attribution, including copying them into another repository or placing them in an LLM prompt.
