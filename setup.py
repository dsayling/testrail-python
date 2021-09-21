from setuptools import setup

setup(
    use_scm_version={'tag_regex': r"^(?P<prefix>example-)?(?P<version>[vV]?\d+(?:\.\d+){0,2}[^\+]*)(?:\+.*)?$"}
    )
