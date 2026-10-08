"""Canonical Japanese changelog source for daitai."""

from shikumi_devdoc.fields.changelog import added
from shikumi_devdoc.norms.common import canonical_source
from shikumi_devdoc.norms.document import title


@canonical_source(
    "daitai 変更履歴",
    filename="CHANGELOG.md",
    merge_policy="forbidden",
    heading="title",
)
class CHANGELOG:
    """`daitai` の変更履歴を日付単位で記録する。"""

    class D2026_10_08:
        """daitai の最初の文書一式を作成した。"""

        title @= "2026-10-08"

        added @= "構造化された YAML を LLM が読むための、ドメインフリーな reading convention として daitai を定義した。"
        added @= "LLM 向けの中核文書 `HOW_TO_READ_DAITAI.md` と、提供される読み方を参照する `DAITAI_CHEATSHEET.md` を追加した。"
        added @= "`da.` を、daitai から読み方が提供されていることを示すプレフィクスとして定義した。"
        added @= "意図、重要事項、順序、条件、因果、参照、再利用、集合の性質、意味上の区切りについて初期の読み方を提供した。"
        added @= "shikumi-devdoc による正本文書管理、文書生成スクリプト、ruff・basedpyright・pytest を実行する CI を追加した。"
