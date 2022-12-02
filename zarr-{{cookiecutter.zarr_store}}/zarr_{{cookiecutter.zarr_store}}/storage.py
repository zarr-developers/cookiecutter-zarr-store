"""This module contains {{ cookiecutter.zarr_store}} storage classes for use with Zarr arrays and groups.

Note that any object implementing the :class:`MutableMapping` interface from the
:mod:`collections` module in the Python standard library can be used as a Zarr
array store, as long as it accepts string (str) keys and bytes values.

In addition to the :class:`MutableMapping` interface, store classes may also implement
optional methods `listdir` (list members of a "directory") and `rmdir` (remove all
members of a "directory"). These methods should be implemented if the store class is
aware of the hierarchical organisation of resources within the store and can provide
efficient implementations. If these methods are not available, Zarr will fall back to
slower implementations that work via the :class:`MutableMapping` interface. Store
classes may also optionally implement a `rename` method (rename all members under a given
path) and a `getsize` method (return the size in bytes of a given value).

"""

from zarr._storage.store import Store as BaseStore
from numcodecs.compat import ensure_bytes


class Store(BaseStore):
    """Storage class using {{ cookiecutter.zarr_store}}.

    .. note:: This is an experimental feature.

    Parameters
    ----------
    dimension_separator : {'.', '/'}, optional
        Separator placed between the dimensions of a chunk.
    **kwargs
        Keyword arguments passed through to the `redis.Redis` function.

    """
    def __init__(self, client=None, dimension_separator=None, **kwargs):

        # Import backend implementation here
        # As a temporary measure, we are using an internal dictionary.
        if client is None:
            client = {}
        self.client = client

        self._kwargs = kwargs
        self._dimension_separator = dimension_separator

    def _key(self, key):
        """
        Can be used to map the key for local purposes.
        """
        return key

    def __getitem__(self, key):
        return self.client[self._key(key)]

    def __setitem__(self, key, value):
        value = ensure_bytes(value)
        self.client[self._key(key)] = value

    def __delitem__(self, key):
        del self.client[self._key(key)]

    def keylist(self):
        return self.client.keys()

    def keys(self):
        yield from self.keylist()

    def __iter__(self):
        yield from self.keys()

    def __len__(self):
        return len(self.keylist())

    def __getstate__(self):
        return self.client, self._dimension_separator, self._kwargs

    def __setstate__(self, state):
        client, dimension_separator, kwargs = state
        self.__init__(client=client,
                      dimension_separator=dimension_separator,
                      **kwargs)

    def clear(self):
        for key in list(self.keys()):
            del self[key]
