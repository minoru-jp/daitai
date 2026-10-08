"""Canonical Japanese project-status source for daitai."""

from shikumi_devdoc.norms.common import canonical_source
from shikumi_devdoc.norms.document import title


@canonical_source(
    "daitai Project Status",
    filename="STATUS.md",
    merge_policy="local",
    heading="title",
)
class PROJECT_STATUS:
    r"""
    `daitai` の現在の設計方針と検討状況を記述する。過去の変更は [CHANGELOG](CHANGELOG.md) が担当する。
    """

    class STATUS_001:
        r"""
        daitai は初期段階にある。実際の利用を通して、reading convention と `da.*` が提供する読み方、作例を見直していく。
        """

        title @= "開発段階"

    class STATUS_002:
        r"""
        daitai は、**YAML を通じて意図と構造を LLM に伝えるための reading convention** である。通常の YAML を使い、厳密な schema を必要としない。
        """

        title @= "目的"

    class STATUS_003:
        r"""
        `*.daitai.yml` と `*.daitai.yaml` を、daitai の reading convention を適用する YAML 文書のファイル名として扱う。通常の `*.yml` と `*.yaml` には、ファイル名だけを根拠として daitai の読み方を仮定しない。

        `.daitai` は別形式を導入するものではなく、その YAML に daitai の reading convention を適用することを示すファイル名上の印である。
        """

        title @= "ファイル名による識別"

    class STATUS_004:
        r"""
        読み手は LLM であり、専用パーサやバリデータを前提にしない。通常の YAML の構造と自然言語を合わせて読み、対象の種類を固定した型体系ではなく、名前と文脈から意味を判断する。

        文書構成では [HOW_TO_READ_DAITAI.md](../HOW_TO_READ_DAITAI.md) を中核とする。daitai が提供する読み方と `da.*` の語彙も、この文書に集約する。
        """

        title @= "文書の中心"

    class STATUS_005:
        r"""
        `da.` は、その記述について daitai から読み方が提供されていることを示すプレフィクスとして扱う。

        提供された読み方は `da.intent` のようにそのまま使うことも、`da.intent.primary` や `da.when.viewport_narrow` のように後続の名前で具体化することもできる。後続部分は通常の言葉として文脈から読む。値の形や後続名の深さを固定しない。

        新しい読み方を追加するときは、通常の YAML と自然文だけでは関係を取り違えやすく、あらかじめ共有された読み方を提供する価値があるかを主な判断基準にする。
        """

        title @= "`da.` が提供する読み方"

    class STATUS_006:
        r"""
        リポジトリ直下は `README.md`、`HOW_TO_READ_DAITAI.md`、`LICENSE` を中心とする公開面として保ち、文書生成・検証・プロジェクト管理に関するファイルは `dev/` にまとめる。GitHub Actions と Git のメタデータは、それぞれの仕組みが要求する場所に置く。
        """

        title @= "リポジトリ構成"

    class STATUS_007:
        r"""
        作例には、写真整理アプリなど現在の主な利用場面に近い題材を使う。
        """

        title @= "作例"
