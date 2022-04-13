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
    tree.insert(1, 5)
    tree.insert(1, 6)

    print_tree(tree)
    
    other = AVLTreeList()
    other.insert(0, 8)
    other.insert(1, 9)
    other.insert(1, 10)
    other.insert(3, 11)

    print_tree(other)

    tree.concat(other)
    print_tree(tree)

    arr_tree = tree.listToArray()
    if arr_tree.length != 5:
        print("Error in listToArray()")
    for i in range(arr_tree.length):
        if arr_tree[i] != tree.retrieve(i):
            print("Error in listToArray()")

    splitted_tree = tree.split(4)
    if splitted_tree[0].size != 4 or splitted_tree[1] != 4 or splitted_tree[2] != None:
        print("Error in split(i)")

    concat_tree = AVLTreeList()
    concat_tree.insert(0, 6) #       6
    concat_tree.insert(0, 5) #   5       7
    concat_tree.insert(2, 7) #
    if (tree.concat(concat_tree) != 3):
        print("Error in concat(t)")

    if (tree.search(4) != 4 or tree.search(100) != -1):
        print("Error in search(val)")

tester()