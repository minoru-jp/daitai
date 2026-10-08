<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `devdocs/canonical_sources/changelog/canonical.py` です。
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

# daitai 変更履歴

`daitai` の変更履歴を日付単位で記録する。

## 2026-10-08

daitai の最初の文書一式を作成した。

Added:

- 構造化された YAML を LLM が読むための、ドメインフリーな reading convention として daitai を定義した。
- LLM 向けの中核文書 `HOW_TO_READ_DAITAI.md` と、提供される読み方を参照する `DAITAI_CHEATSHEET.md` を追加した。
- `da.` を、daitai から読み方が提供されていることを示すプレフィクスとして定義した。
- 意図、重要事項、順序、条件、因果、参照、再利用、集合の性質、意味上の区切りについて初期の読み方を提供した。
- shikumi-devdoc による正本文書管理、文書生成スクリプト、ruff・basedpyright・pytest を実行する CI を追加した。
