# flake8: noqa
from zarr_{{ cookiecutter.zarr_store}}.storage import *
from zarr._storage.store import v3_api_available

# in case setuptools scm screw up and find version to be 0.0.0
from zarr_{{ cookiecutter.zarr_store}}.version import version as __version__
assert not __version__.startswith("0.0.0")
