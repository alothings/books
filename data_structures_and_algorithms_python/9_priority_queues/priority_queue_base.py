"""
Code Fragment 9.1

Priority Queue base class from book
"""


class PriorityQueueBase:
    """ Abstract base class for a PQ"""

    class _Item:
        """ Lightweight composite to store PQ items """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key   # true if less than other

    def is_empty(self):     # concrete method assuming abstract len
        return len(self) == 0
