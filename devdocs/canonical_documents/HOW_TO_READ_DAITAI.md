<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `devdocs/canonical_sources/guides/__init__.py` です。
直接編集しないでください。

公開文書作成方針

- `devdocs/canonical_documents/` にある日本語 canonical document を公開工程の入力とし、英語へ翻訳する。
- 翻訳では意味、構造、情報量を維持し、内容を勝手に追加・削除・要約しない。
- `da.` で始まるキーは、daitai から読み方が提供されている記述として扱い、キー自体は翻訳・変更しない。
- `branch`、`extension`、`restriction`、`replacement` など、`da.*` の値として例示される英語の慣用表現は変更しない。
- YAML 例の値（自然文）は英語へ翻訳する。設計者が自由に付ける名前（YAML のキー）は、日本語なら自然な英語の名前へ置き換えてよく、英語ならそのまま保つ。
- コード、コマンド、ファイルパス、URL は、翻訳上の必要がない限り変更しない。
- このコメントブロックは published document には含めない。
- published document は canonical document から派生する公開成果物として扱い、内容の変更が必要な場合は canonical source へ戻して canonical document を再生成する。
-->

# How to Read daitai

この文書は、構造化された YAML を daitai の reading convention に沿って読む LLM のためのガイドである。対象の YAML を読む前に、この文書を読むこと。

## 読み方の原則

daitai は、構造化された YAML の記述を LLM がどう読むかを共有するための、ドメインフリーな **reading convention** である。

読むときは、次の原則を使う。

1. **YAML として読む。** mapping、sequence、scalar、インデントなどは通常の YAML として解釈する。
2. **キー名を言葉として読む。** キーを単なるフィールド名や ID と決めつけず、その名前自体の意味を周囲の文脈と合わせて解釈する。
3. **構造そのものを記述として読む。** 名前がどこに置かれ、何と並び、何を内包しているかも意味の一部である。その構造が分類・所属などの意味上の関係を表すのか、構成・配置・順序などのデザインを表すのか、あるいは両方なのかを文脈から判断する。

たとえば次の記述では、`about_gui_design`、`main_window`、`sidebar`、`photo_grid` という名前だけでなく、その階層そのものも説明である。

```yaml
about_gui_design:
  main_window:
    sidebar: 左側。アルバムとタグ
    photo_grid: 中央。写真をサムネイルで一覧する
```

`about_gui_design` を具体的な GUI component と決めつける必要はない。名前と構造を合わせて、「GUI 設計についての文脈の中に main window があり、その中に sidebar と photo grid がある」と読む。その構造から、意味上の包含だけでなく画面構成のイメージも読み取れる。

## `da.*` が提供する読み方

`da.` プレフィクスは、**その記述について daitai から読み方が提供されていること**を示す。`da.` がない場所は、通常の YAML と自然言語として読む。

提供された読み方は、プレフィクスの後ろ全体に及ぶ場合も、途中までに及ぶ場合もある。

- `da.intent` は語全体として読み方が提供されている。
- `da.group.exclusive` では、`group` までが「集合について述べる」という読み方として提供され、`exclusive` は通常の名前として読む。

文書にない名前が `da.` の下に現れた場合も、提供されている部分の読み方を適用し、残りはキー名、値、構造、周囲の文脈から解釈する。

| 語 | 提供される読み方 |
| --- | --- |
| `da.intent` | 対象やまとまりの目的、役割、意図 |
| `da.important` | 具体化しても失ってはいけない意図や制約 |
| `da.items` | 順序に意味がある項目の列 |
| `da.separator` | 前後の内容に意味上の区切りがあること |
| `da.group.*` | 複数の項目からなる集合について、`*` に書かれた性質や関係を適用する |
| `da.when` | 条件付きの内容 |
| `da.relation` | 条件付き内容と通常時の内容の関係 |
| `da.target` | 操作・処理・イベントが主に作用する対象 |
| `da.trigger` | 処理や変化が始まるきっかけ |
| `da.outcome` | 結果として成立する状態、効果、生成物 |
| `da.ref` | 別の名前付き対象への意味的な言及 |
| `da.use` | 別の場所に書かれた構造や記述を、この位置でも使う・適用する |

値の形を厳密な型として扱わない。提供された読み方と、通常の YAML・言葉・構造の読み方を合わせて解釈する。

## 集合と区切り

`da.group.*` は、複数の項目からなる集合について、YAML の階層だけでは表しにくい性質や関係を伝えるための読み方である。`*` は固定語彙ではなく、通常の名前として読む。

```yaml
display_mode:
  da.group.exclusive: true
  list:
  grid:
  compact:
```

この場合は、周囲の構造から `list`、`grid`、`compact` を集合として捉え、`exclusive` をその集合の性質として読む。

対象を値の側で明示することもできる。

```yaml
toolbar:
  da.group.exclusive:
    items:
      - select
      - draw
      - erase
```

`true` なら周囲から対象集合を判断し、値に項目や構造があれば、それを対象を特定する情報として読む。`items` のような内側のキーも通常の名前として解釈する。

`da.separator` は集合そのものではなく、前後に意味上の境界があることを示す。

```yaml
menu:
  da.items:
    - open
    - save
    - da.separator: true
    - quit
```

境界を具体的にどう表現するかは、その対象と文脈から判断する。
