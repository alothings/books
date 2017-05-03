"""
Tree ADT using the concept of position
This class has mostly accessors.
It doesn't define how elements are stored

"""
from collections import deque
import queue

class Tree:
    """ Abstract base class representing tree struct"""

    # ---------- nested Position class -----------
    class Position:
        """ Abstraction representing location of each element"""
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Not equal, opposite of eq"""
            return not(self == other)

    # ---- abstract methods that concrete subclasses must support
    def root(self):
        """ return position tree's root"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """ return position of parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """ return # of children that position p has """
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """ Generate iteration of p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    # ----------- concrete methods implemented in this class
    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def __iter__(self):
        """ Generate an iteration of the tree's elements. 
        Needs a T.positions(): Generator of all positions of tree
        Will be implemented by traversals
        """
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder()

    # --------- Traversing Preorder  -------------------

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

    # ---------- Preorder indented ------------------

    def preorder_indent(self, p, d):
        print(2*d*' ' + str(p.element()))
        for c in self.children(p):
            self.preorder_indent(self, c, d+1)

    # ---------- Postorder Traversal ----------------------
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postoder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    # --------- Breadth First traversal  ------------------
    def breadthfirst(self):
        """ Generates iterator by levels"""
        if not self.is_empty():         # why is it called fringe?
            fringe = deque()
            fringe.append(self.root())
            while fringe:
                p = fringe.popleft()
                yield p
                for c in self.children(p):
                    fringe.append(c)


    # ----------- depth method -------
    def depth(self, p):
        if self.is_root(p): return 0
        else:
            return 1 + self.depth(self.parent(p))

    # ----------- heights methods ----
    def _height2(self, p):
        """ recursively """
        if self.is_leaf(p): return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)