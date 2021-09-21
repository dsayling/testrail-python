from setuptools import setup

setup(
    use_scm_version=dict(tag_regex=r"^(?P<prefix>example-)?(?P<version>[vV]?\d+(?:\.\d+){0,2}[^\+]*)(?:\+.*)?$")
    )
