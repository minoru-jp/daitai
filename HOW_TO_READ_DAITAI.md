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

A provided reading can be used as-is or refined by continuing the key with additional names. Read those additional names as ordinary language and combine them with the provided reading.

- `da.intent` and `da.intent.primary` both use the provided reading for `intent`; read `primary` as an ordinary name.
- `da.when` and `da.when.viewport_narrow` likewise use the reading for `when`, with the remainder interpreted from its name and context.
- In `da.group.exclusive`, the reading for `group` is followed by the ordinary name `exclusive`.

If an undocumented name appears under `da.`, apply any provided reading that matches a known portion, then interpret the remainder from its key name, value, structure, and surrounding context.

| Word | Provided reading |
| --- | --- |
| `da.intent` | Purpose, role, or intent of a subject or grouping |
| `da.important` | Intent or constraints that must survive concretization |
| `da.items` | A sequence of items whose order matters |
| `da.separator` | A semantic boundary between the content before and after it |
| `da.group` | A statement about a group of items |
| `da.when` | Conditional content |
| `da.relation` | Relationship between conditional content and the normal case |
| `da.target` | The main subject acted on by an operation, process, or event |
| `da.trigger` | What causes a process or change to begin |
| `da.outcome` | The resulting state, effect, or output |
| `da.ref` | A semantic reference to another named subject |
| `da.use` | Use or apply a structure or description defined elsewhere at this location |

Do not assume a fixed input pattern or value type for `da.*`. Read the key name, value, and surrounding YAML structure together.

## Do not assume a fixed shape

The same provided reading can be expressed through different YAML shapes. Read the whole structure as ordinary YAML instead of assuming one form in advance.

For example, all three of the following can describe a group with the property `exclusive`.

```yaml
display_mode:
  da.group.exclusive:
    foo:
    bar:
```

```yaml
display_mode:
  da.group.exclusive: true
  foo:
  bar:
```

```yaml
display_mode:
  da.group.exclusive: [foo, bar]
```

`da.when` can likewise express a condition in a continued key or in the value structure.

```yaml
panel:
  da.when.viewport_narrow:
    hidden: true
```

```yaml
panel:
  da.when:
    viewport_narrow:
      hidden: true
```

`da.ref` can also be used on its own or with additional names.

```yaml
profile_card:
  da.ref: user_profile
```

```yaml
profile_card:
  da.ref.primary: user_profile
```

Punctuation may be used to visually separate part of a key. Do not assume that such punctuation has daitai-specific syntax; interpret it as part of the name together with the surrounding context.

```yaml
profile_card:
  da.ref.[a.b]: display_name
```

```yaml
profile_card:
  da.ref.(a.b): display_name
```

Neither `[]` nor `()` is specially prescribed. Here as elsewhere, read the key name and the whole structure as description.

`da.separator` indicates a semantic boundary between what comes before and after it.

```yaml
menu:
  da.items:
    - open
    - save
    - da.separator: true
    - quit
```
