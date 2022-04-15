from avl_skeleton import *
from printree import *

def print_tree(tree):
    print(tree.listToArray())
    for line in printree(tree.root):
        print(line)

def tester():
    tree = AVLTreeList()
    
    tree.insert(0, 0)
    print_tree(tree)
    tree.insert(1, 1)
    print_tree(tree)
    tree.insert(2, 2)
    print_tree(tree)
    tree.insert(3, 3)
    print_tree(tree)
    tree.insert(4, 4)


    print_tree(tree)
    print(tree.first())
    print(tree.last())

tester()