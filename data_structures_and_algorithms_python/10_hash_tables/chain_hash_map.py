"""

"""
from .hash_map_base import HashMapBase
from .unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """ Hash map implemented with separate chaining """

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        pass

    def _bucket_delitem(self, j, k):
        pass

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

