<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `devdocs/canonical_sources/readme/canonical.py` です。
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

# daitai

**daitai** は、構造化された YAML の記述を LLM がどう読むかを共有するための、ドメインフリーな **reading convention** です。

書き手は通常の YAML を自由に使い、名前、階層、scalar の自然文で伝えたいことを書きます。読み手となる LLM には [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) を渡し、その読み方に沿って記述を解釈させます。

## 基本

```yaml
about_gui_design:
  main_window:
    sidebar: 左側。アルバムとタグ
    photo_grid: 中央。写真をサムネイルで一覧する

import_pipeline:
  da.trigger: ユーザーがフォルダを選んで取り込みを開始する
  da.outcome: 写真をライブラリへ登録する
```

`about_gui_design` や `main_window` は固定された型名ではありません。LLM は、キーの名前、インデントによる構造、scalar、周囲の文脈を合わせて読みます。

`da.` は、その記述について daitai から読み方が提供されていることを示すプレフィクスです。`da.*` の読み方を使いたいときは [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md) を参照してください。

## 使い方

1. 通常の YAML で、伝えたいことを書く。
2. LLM に [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) と YAML を渡す。
3. 必要なら [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md) から `da.*` の読み方を利用する。

daitai は特定のドメインを前提にしません。何について書かれているかは、実際の名前、構造、自然文から判断します。

## Documentation

- [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md): daitai の中核。LLM に渡す reading convention です。
- [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md): daitai が提供する読み方と `da.*` のクイックリファレンスです。
- [Project Status](STATUS.md): 現在の設計方針と検討状況です。
- [CHANGELOG](CHANGELOG.md): daitai の変更履歴です。

文書は [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc) で管理しています。正本は `devdocs/` にあります（[devdocs/README.md](devdocs/README.md)）。

## License

MIT No Attribution（MIT-0）で公開しています。[`LICENSE`](LICENSE) を参照してください。

著作権表示や許諾文を残す必要はありません。読み方ガイドなどは、自分のリポジトリへのコピーや LLM へのプロンプトへの貼り付けを含め、表示なしで自由にコピー・改変して使えます。
