"""Canonical Japanese source for the devdocs workspace README."""

from shikumi_devdoc.norms.common import canonical_source
from shikumi_devdoc.norms.document import title


@canonical_source(
    "dev/devdocs/",
    filename="README.md",
    merge_policy="local",
    heading="title",
)
class WORKSPACE:
    r"""
    `dev/devdocs/` は、このリポジトリの文書を [shikumi-devdoc](https://github.com/minoru-jp/shikumi-devdoc) で管理するためのワークスペースである。
    """

    class SECTION_001:
        r"""
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
        """

        title @= "構成"

    class SECTION_002:
        r"""
        リポジトリ直下から、次のコマンドで `canonical_documents/` を再生成できる。

        ```bash
        python dev/scripts/render_docs.py
        ```

        `shikumi-devdoc` の CLI はカレントディレクトリを import path に加えないため、このスクリプトがリポジトリ直下を `PYTHONPATH` に追加して CLI を呼び出す。
        """

        title @= "生成"

    class SECTION_003:
        r"""
        公開版は、日本語の canonical document を LLM が英語へ翻訳して作る。翻訳の方針は `config/notice.toml` に記述し、生成物の先頭のコメントとして埋め込まれる。このコメントは公開版には含めない。

        canonical source を変更したら、canonical document を再生成し、対応する公開版の翻訳も更新する。
        """

        title @= "公開版"

    class SECTION_004:
        r"""
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
        """

        title @= "チェック"
