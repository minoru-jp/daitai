# How to Read daitai

This document is a guide for an LLM reading structured YAML with the daitai reading convention. Read this document before reading the target YAML.

## Applicability

**Apply the daitai reading convention to YAML documents whose filenames match `*.daitai.yml` or `*.daitai.yaml`.**

Do not apply the daitai reading convention merely because a file is named `*.yml` or `*.yaml`. `.daitai` does not denote a separate file format; it is a filename marker indicating that the YAML document is to be read using this reading convention.

## Reading principles

daitai is a **reading convention for conveying intent and structure to LLMs through YAML**. It uses ordinary YAML and does not require a formal schema.

Use these principles when reading:

1. **Read it as YAML.** Interpret mappings, sequences, scalars, indentation, and other structure as ordinary YAML.
2. **Read key names as language.** Do not assume keys are merely field names or IDs. Interpret the meaning of each name together with its surrounding context.
3. **Read structure itself as description.** Where a name appears, what it is beside, and what it contains are all part of the meaning. Infer from context whether the structure expresses semantic relationships such as classification or membership, design such as composition, placement, or order, or both.

For example, in the following description, not only the names `about_gui_design`, `main_window`, `sidebar`, and `photo_grid`, but also their hierarchy is part of the description.

```yaml
about_gui_design:
  main_window:
    sidebar: On the left. Albums and tags
    photo_grid: In the center. Shows photos as thumbnails
```

There is no need to assume that `about_gui_design` is a concrete GUI component. Read the names and structure together: there is a main window in the context of GUI design, with a sidebar and photo grid inside it. From that structure, you can read both semantic containment and an image of the screen composition.

## Readings provided by `da.*`

The `da.` prefix indicates that **daitai provides a reading for that entry**. Where no `da.` key is present, read the content as ordinary YAML and natural language.

A provided reading may cover the entire name after the prefix or only part of it.

- `da.intent` has a provided reading for the whole name.
- In `da.group.exclusive`, `group` provides the reading "about a group", while `exclusive` is read as an ordinary name.

If an undocumented name appears under `da.`, apply the reading provided for any known portion, then interpret the remainder from its key name, value, structure, and surrounding context.

| Word | Provided reading |
| --- | --- |
| `da.intent` | Purpose, role, or intent of a subject or grouping |
| `da.important` | Intent or constraints that must survive concretization |
| `da.items` | A sequence of items whose order matters |
| `da.separator` | A semantic boundary between the content before and after it |
| `da.group.*` | Apply the property or relationship named by `*` to a group of items |
| `da.when` | Conditional content |
| `da.relation` | Relationship between conditional content and the normal case |
| `da.target` | The main subject acted on by an operation, process, or event |
| `da.trigger` | What causes a process or change to begin |
| `da.outcome` | The resulting state, effect, or output |
| `da.ref` | A semantic reference to another named subject |
| `da.use` | Use or apply a structure or description defined elsewhere at this location |

Do not treat value shapes as strict types. Combine the provided reading with the ordinary reading of YAML, language, and structure.

## Groups and separators

`da.group.*` provides a reading for properties or relationships of a group of items that are difficult to express through YAML hierarchy alone. The `*` part is not fixed vocabulary; read it as an ordinary name.

```yaml
display_mode:
  da.group.exclusive: true
  list:
  grid:
  compact:
```

Here, infer the group `list`, `grid`, and `compact` from the surrounding structure, then read `exclusive` as a property of that group.

The target group can also be made explicit in the value.

```yaml
toolbar:
  da.group.exclusive:
    items:
      - select
      - draw
      - erase
```

With `true`, infer the target group from the surroundings. If the value contains items or other structure, use it as information identifying the target. Nested keys such as `items` are also read as ordinary names.

`da.separator` describes a semantic boundary rather than a group itself.

```yaml
menu:
  da.items:
    - open
    - save
    - da.separator: true
    - quit
```

Determine how that boundary should be represented from the subject and context.
