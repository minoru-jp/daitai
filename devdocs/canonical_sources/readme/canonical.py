"""Canonical Japanese README source for daitai."""

from shikumi_devdoc.norms.common import canonical_source
from shikumi_devdoc.norms.document import title


@canonical_source(
    "daitai",
    filename="README.md",
    merge_policy="local",
    heading="title",
)
class README:
    r"""
    **daitai** は、構造化された YAML の記述を LLM がどう読むかを共有するための、ドメインフリーな **reading convention** です。

    書き手は通常の YAML を自由に使い、名前、階層、scalar の自然文で伝えたいことを書きます。読み手となる LLM には [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) を渡し、その読み方に沿って記述を解釈させます。
    """

    class SECTION_001:
        r"""
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
        """

        title @= "基本"

    class SECTION_002:
        r"""
        1. 通常の YAML で、伝えたいことを書く。
        2. LLM に [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md) と YAML を渡す。
        3. 必要なら [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md) から `da.*` の読み方を利用する。

        daitai は特定のドメインを前提にしません。何について書かれているかは、実際の名前、構造、自然文から判断します。
        """

        title @= "使い方"

    class SECTION_003:
        r"""
        - [HOW_TO_READ_DAITAI.md](HOW_TO_READ_DAITAI.md): daitai の中核。LLM に渡す reading convention です。
        - [DAITAI_CHEATSHEET.md](DAITAI_CHEATSHEET.md): daitai が提供する読み方と `da.*` のクイックリファレンスです。
        - [Project Status](STATUS.md): 現在の設計方針と検討状況です。
        - [CHANGELOG](CHANGELOG.md): daitai の変更履歴です。

        文書は [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc) で管理しています。正本は `devdocs/` にあります（[devdocs/README.md](devdocs/README.md)）。
        """

        title @= "Documentation"

    class SECTION_004:
        r"""
        MIT No Attribution（MIT-0）で公開しています。[`LICENSE`](LICENSE) を参照してください。

        著作権表示や許諾文を残す必要はありません。読み方ガイドなどは、自分のリポジトリへのコピーや LLM へのプロンプトへの貼り付けを含め、表示なしで自由にコピー・改変して使えます。
        """

        title @= "License"
