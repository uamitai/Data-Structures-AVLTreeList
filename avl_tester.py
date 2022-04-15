from avl_skeleton import *
from printree import *

def print_tree(tree):
    print(tree.listToArray())
    for line in printree(tree.root):
        print(line)

def insert(tree, val, i):
    tree.insert(i, val)
    print_tree(tree)

def tester():
    tree = AVLTreeList()
    
    insert(tree, 8, 0)
    insert(tree, 5, 0)
    insert(tree, 10, 2)
    insert(tree, 4, 0)
    insert(tree, 6, 2)

    tree.delete(4)
    print_tree(tree)

tester()