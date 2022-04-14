from avl_skeleton import *
from printree import *

def print_tree(tree):
    print(tree.listToArray())
    for line in printree(tree.root):
        print(line)

def tester():
    tree = AVLTreeList()
    
    tree.insert(0, 0)
    tree.insert(1, 1)
    tree.insert(0, 2)
    tree.insert(2, 3)
    tree.insert(4, 4)
    tree.insert(4, 5)
    tree.insert(4, 6)
    tree.insert(3, 7)
    tree.insert(1, 8)
    tree.insert(0, 9)

    print_tree(tree)
    
    other = AVLTreeList()
    """other.insert(0, 5)
    other.insert(1, 9)
    other.insert(1, 10)
    other.insert(3, 11)"""

    lst = tree.split(9)
    print_tree(lst[0])
    print(lst[1])
    print_tree(lst[2])

    """
    lst = tree.split(1)
    print_tree(lst[0])
    print(lst[1])
    print_tree(lst[2])
    """

tester()