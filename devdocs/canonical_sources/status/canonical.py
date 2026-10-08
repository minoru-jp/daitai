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
        daitai は、構造化された YAML を LLM が読むための、ドメインフリーな **reading convention** である。

        何について書かれているかを事前に限定せず、キー名、階層、scalar の自然文、周囲の文脈から判断する。
        """

        title @= "対象範囲"

    class STATUS_003:
        r"""
        読み手は LLM であり、専用パーサやバリデータを前提にしない。通常の YAML の構造と自然言語を合わせて読み、対象の種類を固定した型体系ではなく、名前と文脈から意味を判断する。

        文書構成では [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) を中核とする。daitai が提供する読み方と `da.*` の語彙も、この文書に集約する。
        """

        title @= "文書の中心"

    class STATUS_004:
        r"""
        `da.` は、その記述について daitai から読み方が提供されていることを示すプレフィクスとして扱う。

        読み方は `da.intent` のように語全体へ提供することも、`da.group.*` のように途中まで提供することもできる。後者では、その先の名前を通常の言葉として文脈から読む。

        新しい読み方を追加するときは、通常の YAML と自然文だけでは関係を取り違えやすく、あらかじめ共有された読み方を提供する価値があるかを主な判断基準にする。
        """

        title @= "`da.` が提供する読み方"

    class STATUS_005:
        r"""
        作例には、写真整理アプリなど現在の主な利用場面に近い題材を使う。作例のドメインは reading convention の適用範囲を限定しない。
        """

        title @= "作例"
