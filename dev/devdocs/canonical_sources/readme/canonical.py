"""Canonical Japanese README source for daitai."""

from shikumi_devdoc.norms.common import canonical_source


@canonical_source(
    "daitai",
    filename="README.md",
    merge_policy="local",
    heading="title",
)
class README:
    r"""
    [HOW_TO_READ_DAITAI](HOW_TO_READ_DAITAI.md)
    """
