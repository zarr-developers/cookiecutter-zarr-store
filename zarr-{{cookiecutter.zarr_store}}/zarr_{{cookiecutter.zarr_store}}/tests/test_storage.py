from zarr_{{ cookiecutter.zarr_store}}.storage import Store
from zarr.tests.test_storage import StoreTests, dimension_separator_fixture


class TestStore(StoreTests):

    def create_store(self, **kwargs):
        store = Store(**kwargs)
        # start with an empty store
        store.clear()
        return store
