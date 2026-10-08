<!--
この文書は `shikumi-devdoc` によって生成された canonical document です。
Canonical source は `devdocs/canonical_sources/status/canonical.py` です。
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

# daitai Project Status

`daitai` の現在の設計方針と検討状況を記述する。過去の変更は [CHANGELOG](CHANGELOG.md) が担当する。

## 開発段階

daitai は初期段階にある。実際の利用を通して、reading convention と `da.*` が提供する読み方、作例を見直していく。

## 対象範囲

daitai は、構造化された YAML を LLM が読むための、ドメインフリーな **reading convention** である。

何について書かれているかを事前に限定せず、キー名、階層、scalar の自然文、周囲の文脈から判断する。

## 文書の中心

読み手は LLM であり、専用パーサやバリデータを前提にしない。通常の YAML の構造と自然言語を合わせて読み、対象の種類を固定した型体系ではなく、名前と文脈から意味を判断する。

文書構成では [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) を中核とする。daitai が提供する読み方と `da.*` の語彙も、この文書に集約する。

## `da.` が提供する読み方

`da.` は、その記述について daitai から読み方が提供されていることを示すプレフィクスとして扱う。

読み方は `da.intent` のように語全体へ提供することも、`da.group.*` のように途中まで提供することもできる。後者では、その先の名前を通常の言葉として文脈から読む。

新しい読み方を追加するときは、通常の YAML と自然文だけでは関係を取り違えやすく、あらかじめ共有された読み方を提供する価値があるかを主な判断基準にする。

## 作例

作例には、写真整理アプリなど現在の主な利用場面に近い題材を使う。作例のドメインは reading convention の適用範囲を限定しない。
