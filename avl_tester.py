def tester():
    tree = AVLTreeList()
    for i in range(5):
        tree.insert(i, i)

    if tree.empty:
        print("Error in empty() or insert(i, j)")
    if tree.size != 5:
        print("Error in size()")
    if tree.retrieve(3) != 3:
        print("Error in retrieve(i)")

    tree.delete(2)

    if tree.size != 4:
        print("Error in delete(i)")
    if tree.first != 0:
        print("Error in first()")
    if tree.last != 4:
        print("Error in last()")

    tree.insert(2, 2)
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