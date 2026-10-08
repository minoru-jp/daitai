# daitai Cheat Sheet

A quick reference for the readings provided by daitai. For the complete LLM-side reading convention, see [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md).

## Reading essentials

1. **Read it as YAML.** Interpret mappings, sequences, scalars, indentation, and other structure as ordinary YAML.
2. **Read key names as language.** Interpret the meaning of each key name together with its surrounding context.
3. **Read structure itself as description.** Infer from context whether hierarchy and arrangement express semantic relationships, design such as composition, placement, or order, or both.

The `da.` prefix indicates that daitai provides a reading for that entry.

## `da.*` reference

| Word | Provided reading |
| --- | --- |
| `da.intent` | Purpose, role, or intent |
| `da.important` | Intent or constraints that must survive concretization |
| `da.items` | An ordered sequence of items |
| `da.separator` | A semantic boundary between the content before and after it |
| `da.group.*` | Apply the property or relationship named by `*` to a group |
| `da.when` | Conditional content |
| `da.relation` | Relationship between conditional content and the normal case |
| `da.target` | Subject acted on by an operation, process, or event |
| `da.trigger` | What starts a process or change |
| `da.outcome` | Resulting state, effect, or output |
| `da.ref` | Semantic reference to another named subject |
| `da.use` | Use or apply a structure or description defined elsewhere |

As with the `*` in `da.group.*`, a daitai-provided reading may stop before the end of a name, leaving the remainder to be read as ordinary language. Value shapes are also not fixed; read the key name, value, hierarchy, and surrounding context together.

## Names and hierarchy

```yaml
about_product:
  photo_library: A desktop app for organizing and searching local photos

about_gui_design:
  main_window:
    sidebar: On the left. Albums and tags
    photo_grid: In the center. Shows photos as thumbnails

about_backend:
  import_pipeline:
    da.intent: Safely import photos into the library
```

`about_product` and `about_gui_design` are not daitai vocabulary. Their names and contents establish context.

## Intent, processes, and important constraints

```yaml
import_pipeline:
  da.target: The selected photo files
  da.trigger: The user starts importing
  da.outcome: Register the photos in the library and generate thumbnails

important_constraints:
  da.important: Do not modify the original photo files
```

## Conditions and relationships

```yaml
import_pipeline:
  da.when:
    The same file is already registered:
      da.relation: restriction
      da.outcome: Do not register it twice; point to the existing photo
```

For `da.relation`, conventional short terms such as `branch`, `extension`, `restriction`, and `replacement` can be useful, but natural language can be read as well.

## Order

```yaml
startup_sequence:
  da.items:
    - Load configuration
    - Open the database
    - Start background processing
    - Show the main window
```

## Groups and separators

```yaml
display_mode:
  da.group.exclusive: true
  list:
  grid:
  compact:

toolbar:
  da.group.exclusive:
    items:
      - select
      - draw
      - erase

menu:
  da.items:
    - open
    - save
    - da.separator: true
    - quit
```

- `da.group.*` provides a foothold for reading a property or relationship of a group from the name in `*`.
- With `true`, infer the relevant group from the surroundings. If the value contains items or structure, use that information to identify the target group.
- `da.separator` marks a semantic boundary without prescribing its concrete representation.

## References and reuse

```yaml
export_job:
  source:
    da.ref: current photo_selection

desktop_app:
  import_behavior:
    da.use: import_pipeline
```

- `da.ref` is a semantic reference.
- `da.use` applies a structure or description from another location here.
