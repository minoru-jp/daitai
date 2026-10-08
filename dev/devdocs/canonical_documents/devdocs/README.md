<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `dev/devdocs/canonical_sources/workspace/canonical.py` です。
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

# dev/devdocs/

`dev/devdocs/` は、このリポジトリの文書を [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc) で管理するためのワークスペースである。

## 構成

```text
dev/
├── CHANGELOG.md
├── STATUS.md
├── pyproject.toml
├── requirements-dev.txt
├── scripts/
├── tests/
└── devdocs/
    ├── canonical_sources/    正本（Python）
    │   ├── readme/
    │   ├── status/
    │   ├── changelog/
    │   ├── guides/           HOW_TO_READ_DAITAI
    │   └── workspace/        この README
    ├── config/
    │   └── notice.toml       生成物の先頭に埋め込む注意書きと公開方針
    └── canonical_documents/  正本から生成した日本語の文書
```

- `canonical_sources/` の Python が文書の正本である。文書を変更するときはここを編集する。
- `canonical_documents/` は生成物である。レビューのために Git に含めるが、直接編集しない。
- リポジトリ直下の `README.md` と `HOW_TO_READ_DAITAI.md`、`dev/` にある `STATUS.md` と `CHANGELOG.md`、およびこの `dev/devdocs/README.md` は、`canonical_documents/` を英語へ翻訳した公開版である。

## 生成

リポジトリ直下から、次のコマンドで `canonical_documents/` を再生成できる。

```bash
python dev/scripts/render_docs.py
```

`shikumi-devdoc` の CLI はカレントディレクトリを import path に加えないため、このスクリプトがリポジトリ直下を `PYTHONPATH` に追加して CLI を呼び出す。

## 公開版

公開版は、日本語の canonical document を LLM が英語へ翻訳して作る。翻訳の方針は `config/notice.toml` に記述し、生成物の先頭のコメントとして埋め込まれる。このコメントは公開版には含めない。

canonical source を変更したら、canonical document を再生成し、対応する公開版の翻訳も更新する。

## チェック

`dev/` で開発用の依存関係をインストールし、次を実行する。

```bash
cd dev
python -m pip install -r requirements-dev.txt
ruff format --check .
ruff check .
basedpyright
pytest
```

テストでは、canonical document が正本と同期していること、各文書の YAML 例が通常の YAML として読めて同じ mapping に重複キーがないこと、公開版が揃っていることを確認する。daitai の意味上の妥当性は検証しない。

GitHub Actions（`.github/workflows/checks.yml`）は、`main` への push と pull request のたびに、Python 3.11 で同じチェックを実行する。公開版の翻訳が canonical document に追いついているかは、CI では確認しない。
