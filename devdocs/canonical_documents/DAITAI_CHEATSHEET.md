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

# daitai Cheat Sheet

daitai が提供する読み方を素早く確認するための一覧です。LLM 側の完全な読み方は [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) を参照してください。

## 読み方の要点

1. **YAML として読む。** mapping、sequence、scalar、インデントなどは通常の YAML として解釈する。
2. **キー名を言葉として読む。** キー名そのものの意味を、周囲の文脈と合わせて読む。
3. **構造そのものを記述として読む。** 階層や並びが、意味上の関係、構成・配置・順序などのデザイン、またはその両方を表すかを文脈から判断する。

`da.` は、その記述について daitai が読み方を提供していることを示す。

## `da.*` 一覧

| 語 | 提供される読み方 |
| --- | --- |
| `da.intent` | 目的・役割・意図 |
| `da.important` | 具体化しても失ってはいけない意図・制約 |
| `da.items` | 順序に意味がある項目の列 |
| `da.separator` | 前後に意味上の区切りがあること |
| `da.group.*` | 集合について、`*` に書かれた性質・関係を適用する |
| `da.when` | 条件付きの内容 |
| `da.relation` | 条件付き内容と通常時の内容の関係 |
| `da.target` | 操作・処理・イベントが作用する対象 |
| `da.trigger` | 処理や変化のきっかけ |
| `da.outcome` | 結果として成立する状態・効果・生成物 |
| `da.ref` | 別の名前付き対象への意味的な言及 |
| `da.use` | 別の場所の構造や記述をここでも使う・適用する |

`da.group.*` の `*` のように、daitai が読み方を提供した先を通常の名前として読むことがあります。値の形も固定せず、キー名、値、階層、周囲の文脈を合わせて読みます。

## 名前と階層

```yaml
about_product:
  photo_library: ローカルの写真を整理・検索するデスクトップアプリ

about_gui_design:
  main_window:
    sidebar: 左側。アルバムとタグ
    photo_grid: 中央。写真をサムネイルで一覧する

about_backend:
  import_pipeline:
    da.intent: 写真をライブラリへ安全に取り込む
```

`about_product` や `about_gui_design` は daitai の語彙ではありません。名前と内側の内容から文脈を伝えています。

## 意図・処理・重要事項

```yaml
import_pipeline:
  da.target: 選択された写真ファイル
  da.trigger: ユーザーが取り込みを開始する
  da.outcome: ライブラリへ登録し、サムネイルを生成する

important_constraints:
  da.important: 元の写真ファイルは変更しない
```

## 条件と関係

```yaml
import_pipeline:
  da.when:
    同じファイルが登録済みの場合:
      da.relation: restriction
      da.outcome: 二重登録せず、既存の写真を示す
```

`da.relation` は短い慣用表現として `branch`、`extension`、`restriction`、`replacement` などを使えますが、自然文でも読めます。

## 順序

```yaml
startup_sequence:
  da.items:
    - 設定を読み込む
    - データベースを開く
    - バックグラウンド処理を開始する
    - メインウィンドウを表示する
```

## 集合と区切り

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

- `da.group.*` は、集合について伝えたい性質や関係を `*` の名前から読むための足場です。
- `true` なら周囲から対象集合を読み、値に項目や構造があればそれを対象を特定する情報として読みます。
- `da.separator` は前後の意味上の境界です。具体的な表現方法までは指定しません。

## 参照・再利用

```yaml
export_job:
  source:
    da.ref: 現在の photo_selection

desktop_app:
  import_behavior:
    da.use: import_pipeline
```

- `da.ref` は意味的な言及です。
- `da.use` は別の場所の構造や記述をその位置でも使うことを示します。
