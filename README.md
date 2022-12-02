# Cookiecutter to create Zarr stores

[![Actions Status](https://github.com/zarr-developers/cookiecutter-zarr-store/workflows/Build/badge.svg)](https://github.com/zarr-developers/cookiecutter-zarr-store/actions)

This repository offers a [cookiecutter](https://cookiecutter.readthedocs.io)
for creating your own Zarr store implementation.

To use it:

```sh
pip install cookiecutter
cookiecutter https://github.com/zarr-developers/cookiecutter-zarr-store
```
And answer the questions :smile:

In order to run the tests, be sure to initialize git:
```sh
cd zarr-somethingshort
git init
pip install -e .
pytest .
```
