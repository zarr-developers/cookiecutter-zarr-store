# Cookiecutter to create Zarr stores

[![Actions Status](https://github.com/zarr-developers/cookiecutter-zarr-store/workflows/Build/badge.svg)](https://github.com/zarr-developers/cookiecutter-zarr-store/actions)

This repository offers a [cookiecutter](https://cookiecutter.readthedocs.io)
for creating your own Zarr store implementation.

### Creating a repo from the template

```sh
pip install cookiecutter
cookiecutter https://github.com/zarr-developers/cookiecutter-zarr-store
```
Running `cookiecutter` will print a few questions on your terminal.
For the first question (`zarr_store`), use the name of the store
you want to create. E.g. `zipstore` for Zip Store, `mongodb`
for MongoDBStore and so on.

For remaining questions use the value indicated in the `[ ]`. These are the default values set by the maintainers.

### Once you're done with above setup you can move to

- [storage.py](https://github.com/zarr-developers/zarr-python/blob/main/zarr/storage.py) and start separating the desired store's code and integrating into your repository under `zarr-something-short/storage.py`
- Pick up corresponding tests from [tests_storage.py](https://github.com/zarr-developers/zarr-python/blob/main/zarr/tests/test_storage.py) and start adding them into your repository under `zarr-something-short/tests/tests_storage.py`

### Testing the code

Before running the tests,  install `pytest` via `pip install pytest`

In order to run the tests, be sure to initialize git:
```sh
cd zarr-somethingshort
git init
pip install -e .
pytest .
```
