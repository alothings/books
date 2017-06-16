"""

"""
from .hash_map_base import HashMapBase


class ProbeHashMap(HashMapBase):
    """ Hash map implemented with linear probing for collision 
    resolution"""

    _AVAIL = object()   #sentinal marks locations of previous deletions

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """ Search for key k in bucket at index j.
        Return (success, index) tuple described as follows:
        
        if match found, success is True and index is location
        else: success is False and index denotes first available slot
        
        """

    def _bucket_getitem(self, j, k):
        pass

    def _bucket_setitem(self, j, k, v):

        pass

    def _bucket_delitem(self, j, k):
        pass

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

