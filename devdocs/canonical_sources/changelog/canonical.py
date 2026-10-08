"""Canonical Japanese changelog source for daitai."""

from shikumi_devdoc.fields.changelog import added, changed
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
        added @= "LLM 向けの中核文書 `HOW_TO_READ_DAITAI.md` を追加し、reading convention と提供される `da.*` の読み方を集約した。"
        added @= "`da.` を、daitai から読み方が提供されていることを示すプレフィクスとして定義した。"
        added @= "意図、重要事項、順序、条件、因果、参照、再利用、集合の性質、意味上の区切りについて初期の読み方を提供した。"
        added @= "shikumi-devdoc による正本文書管理、文書生成スクリプト、ruff・basedpyright・pytest を実行する CI を追加した。"

        changed @= "`*.daitai.yml` と `*.daitai.yaml` を、daitai の reading convention を適用する YAML 文書のファイル名として定めた。"
        changed @= "通常の `*.yml` と `*.yaml` には、ファイル名だけを根拠として daitai の reading convention を仮定しないことを明確にした。"
        changed @= "daitai の説明を、YAML を通じて意図と構造を LLM に伝える reading convention という目的に焦点を当てた表現へ更新した。"
        changed @= "`da.*` のすべての provided reading で、後続の名前による具体化と複数の値・構造パターンを文脈から読めることを明確にした。"
