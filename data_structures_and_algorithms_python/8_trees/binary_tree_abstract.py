""" 

"""
# import Tree
from .tree_asbtraction import Tree


class BinaryTree(Tree):
    """ abstract base class """

    # ------ abstract methods --------------
    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    # ------ concrete methods implemented in this class
    def sibling(self, p):
        """ return a position representing p's sibling"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

<<<<<<< HEAD
    # -------- inorder traversal ---------------------
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # ------- Overriding inherited versions------------
    def positions(self):
        return self.inorder()
=======
>>>>>>> 0ce49c005bf5f0603043384be104f191c26c43ae

if __name__ == '__main__':
    bt = BinaryTree()
    print("Binary Tree running")