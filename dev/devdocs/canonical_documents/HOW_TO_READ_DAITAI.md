<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `dev/devdocs/canonical_sources/guides/how_to_read.py` です。
直接編集しないでください。

公開文書作成方針

- `dev/devdocs/canonical_documents/` にある日本語 canonical document を公開工程の入力とし、英語へ翻訳する。
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

## 適用対象

**ファイル名が `*.daitai.yml` または `*.daitai.yaml` の YAML 文書には、daitai の reading convention を適用する。**

通常の `*.yml` または `*.yaml` というファイル名だけを根拠に、daitai の reading convention を適用してはならない。`.daitai` は別のファイル形式を表すものではなく、その YAML 文書をこの reading convention で読むことを示すためのファイル名上の印である。

## 読み方の原則

daitai は、**YAML を通じて意図と構造を LLM に伝えるための reading convention** である。記述は通常の YAML として扱い、厳密な schema を必要としない。

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

提供された読み方は、その名前をそのまま使うことも、後ろに名前を続けて具体化することもできる。続いた名前は通常の言葉として読み、提供された読み方と合わせて解釈する。

- `da.intent` と `da.intent.primary` は、どちらも `intent` として提供された読み方を使う。`primary` は通常の名前として読む。
- `da.when` と `da.when.viewport_narrow` も同様に、`when` の読み方を使い、その先は名前と文脈から読む。
- `da.group.exclusive` では、`group` の読み方に `exclusive` という通常の名前が続いている。

文書にない名前が `da.` の下に現れた場合も、提供されている部分の読み方を適用し、残りはキー名、値、構造、周囲の文脈から解釈する。

| 語 | 提供される読み方 |
| --- | --- |
| `da.intent` | 対象やまとまりの目的、役割、意図 |
| `da.important` | 具体化しても失ってはいけない意図や制約 |
| `da.items` | 順序に意味がある項目の列 |
| `da.separator` | 前後の内容に意味上の区切りがあること |
| `da.group` | 複数の項目からなる集合について述べる |
| `da.when` | 条件付きの内容 |
| `da.relation` | 条件付き内容と通常時の内容の関係 |
| `da.target` | 操作・処理・イベントが主に作用する対象 |
| `da.trigger` | 処理や変化が始まるきっかけ |
| `da.outcome` | 結果として成立する状態、効果、生成物 |
| `da.ref` | 別の名前付き対象への意味的な言及 |
| `da.use` | 別の場所に書かれた構造や記述を、この位置でも使う・適用する |

`da.*` に決まった入力パターンや値の型を仮定しない。キー名、値、周囲の YAML 構造を合わせて読む。

## 形を固定しない

同じ provided reading でも、対象や関係の表し方は一つに決まっていない。形を先に決めず、通常の YAML として全体を読む。

たとえば次の三つは、いずれも `exclusive` という性質を持つ集合を表す記述として読める。

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

`da.when` も、条件を後続の名前で表すことも、値の構造で表すこともできる。

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

`da.ref` も同じように、単独でも、後続の名前を伴っても読める。

```yaml
profile_card:
  da.ref: user_profile
```

```yaml
profile_card:
  da.ref.primary: user_profile
```

キーの一部を見た目上区切るために記号が使われることもある。記号には daitai 固有の構文上の意味を仮定せず、名前の一部として周囲と合わせて解釈する。

```yaml
profile_card:
  da.ref.[a.b]: display_name
```

```yaml
profile_card:
  da.ref.(a.b): display_name
```

`[]` と `()` のどちらかが特別に定められているわけではない。ここでも、キー名と構造全体を記述として読む。

`da.separator` は前後に意味上の境界があることを示す。

```yaml
menu:
  da.items:
    - open
    - save
    - da.separator: true
    - quit
```
