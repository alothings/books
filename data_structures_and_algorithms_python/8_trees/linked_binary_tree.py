"""

Implementation of Binary tree as a Linked Structure

"""
# import BinaryTree
from .binary_tree_abstract import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """ Linked representation of bin tree"""

    class _Node:     # lightweight, nonpublic class for storing node
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """ An abstraction representing location of single element"""

        def __init__(self, container, node):
            """ Constructur should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """ return element stored at this position"""
            return self._node._element

        def __eq__(self, other):
            """ return if position represents same location """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """ Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p is not position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # Apparently is a convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Return position instance for given node (or None)"""
        return self.Position(self, node) if node is not None else None

    # ------ binary tree constructor -----------------
    def __init__(self):
        self._root = None
        self._size = 0

    # --------- public accessors ------------------------
    def __len(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        """ return position of p's parent """
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """ return position of p's parent """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """ return position of p's parent """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """ Return the number of children of Position p. """
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    # --------- Traversing!! -------------------
    def preorder(self):
        """ Generate a preorder iteration fo positions"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """ Generate preorder iteration fo position in subtree """

        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other


