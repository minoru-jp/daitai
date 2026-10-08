<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `dev/devdocs/canonical_sources/status/canonical.py` です。
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

# daitai Project Status

`daitai` の現在の設計方針と検討状況を記述する。過去の変更は [CHANGELOG](CHANGELOG.md) が担当する。

## 開発段階

daitai は初期段階にある。実際の利用を通して、reading convention と `da.*` が提供する読み方、作例を見直していく。

## 目的

daitai は、**YAML を通じて意図と構造を LLM に伝えるための reading convention** である。通常の YAML を使い、厳密な schema を必要としない。

## ファイル名による識別

`*.daitai.yml` と `*.daitai.yaml` を、daitai の reading convention を適用する YAML 文書のファイル名として扱う。通常の `*.yml` と `*.yaml` には、ファイル名だけを根拠として daitai の読み方を仮定しない。

`.daitai` は別形式を導入するものではなく、その YAML に daitai の reading convention を適用することを示すファイル名上の印である。

## 文書の中心

読み手は LLM であり、専用パーサやバリデータを前提にしない。通常の YAML の構造と自然言語を合わせて読み、対象の種類を固定した型体系ではなく、名前と文脈から意味を判断する。

文書構成では [HOW_TO_READ_DAITAI.md](../HOW_TO_READ_DAITAI.md) を中核とする。daitai が提供する読み方と `da.*` の語彙も、この文書に集約する。

## `da.` が提供する読み方

`da.` は、その記述について daitai から読み方が提供されていることを示すプレフィクスとして扱う。

提供された読み方は `da.intent` のようにそのまま使うことも、`da.intent.primary` や `da.when.viewport_narrow` のように後続の名前で具体化することもできる。後続部分は通常の言葉として文脈から読む。値の形や後続名の深さを固定しない。

新しい読み方を追加するときは、通常の YAML と自然文だけでは関係を取り違えやすく、あらかじめ共有された読み方を提供する価値があるかを主な判断基準にする。

## リポジトリ構成

リポジトリ直下は `README.md`、`HOW_TO_READ_DAITAI.md`、`LICENSE` を中心とする公開面として保ち、文書生成・検証・プロジェクト管理に関するファイルは `dev/` にまとめる。GitHub Actions と Git のメタデータは、それぞれの仕組みが要求する場所に置く。

## 作例

作例には、写真整理アプリなど現在の主な利用場面に近い題材を使う。
