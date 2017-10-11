"""A module for practicing with Binary Search Trees"""

class BST:
    """A simple binary search tree with no self-balancing"""

    #   Constructors for tree nodes and a two-element tree
    class Node:
        __slots__ = "_value", "_left", "_right"
        def __init__(self, l, v, r):
            self._left = l;
            self._value = v;
            self._right = r
    def __init__(self):
        """This initializes the tree to contain 2 values
        so the minimum function has something to work with"""
        self._root = self.Node(None, 4, self.Node(None, 6, None))

    #   Some methods taht will not need any change during recitation
    def _rec_tuples(self, here):
        """Recursively convert tree into a tuple form"""
        if here is None:
            return ''
        else:
            return (self._rec_tuples(here._left),
                    here._value, self._rec_tuples(here._right))
    def __str__(self):
        """Return a cleaned-up tuple version of the entire tree"""
        tuples = self._rec_tuples(self._root)
        return str(tuples).replace("'', ","").replace(", ''","")

    def max(self):
        """Return maximum value stored in binary search tree"""
        return self._rec_max(self._root)
    def insert(self, value):
        """Insert a single occurrence of given value into the tree"""
        self._root = self._rec_insert(self._root, value)
    def remove(self, value):
        """Remove a single occurrence of given value from the tree"""
        self._root = self._rec_remove(self._root, value)

    #   And three methods to work on during recitation
    def _rec_max(self, here):
        """Recursively seek the largest value in the tree"""
        if here._right == None:
            return here._value
        else:
            return self._rec_max(here._right)
            

    def _rec_insert(self, here, value):
        """Recursively insert a value, returning a new tree"""
        if here is None:
            return self.Node(None, value, None)
        elif value < here._value:
            return self.Node(self._rec_insert(here._left, value), here._value, here._right)
        elif value == here._value:
            return here
        else:
            return self.Node(here._left, here._value, self._rec_insert(here._right, value))
    def _rec_remove(self, here, value):
        """Recursively remove a value once, returning a new value"""
        if here is None:
            return None
        elif value < here._value:
            return self.Node(self._rec_remove(here._left, value), here._value, here._right)
        elif value > here._value:
            return self.Node(here._left, here._value, self._rec_remove(here._right, value))
        elif here._left is None:
            return here._right
        elif here._right is None:
            return here._left
        elif here._left != None and here._right != None:
            move = self._rec_max(here._left)
            return self.Node(self._rec_remove(here._left, move), move, here._right)

# Create a Tree and insert several values
T = BST()
print("Maximum value is", T.max())

inserts = [1,5,2,3,7,0,0,4]
print("Insert ",inserts)
for v in inserts:
    T.insert(v)
    print(T)
print("Maximum value is", T.max())

removes = [0,5,6,2,4]
print("Remove ",removes)
for v in removes:
    T.remove(v)
    print(T)

