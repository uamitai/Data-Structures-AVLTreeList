from avl_skeleton import *
from printree import *
class testAVLList(unittest.TestCase):

<<<<<<< Updated upstream

def tester():
    T = AVLTreeList()
    L = []
    NUM = 6
    for i in range(2*NUM+1):
        T.append(i)
        L.append(i)
    printree(T)
    [T1, val, T2] = T.split(NUM)
    L1 = L[:NUM]
    L2 = L[NUM+1:]
    printree(T1)
    print(T1.length())
    printree(T2)
    print(T2.length())
    
=======
    emptyList = AVLTreeList()
    twentyTree = AVLTreeList()
    twentylist = []
>>>>>>> Stashed changes

    def compare_with_list_by_in_order(self, tree, lst):
        def rec(node, cnt, lst):
            if node.isRealNode():
                rec(node.getLeft(), cnt, lst)
                self.assertEqual(node.getValue(), lst[cnt[0]])
                cnt[0] += 1
                rec(node.getRight(), cnt, lst)

        cnt = [0]
        if not tree.empty():
            rec(tree.getRoot(), cnt, lst)
        else:
            self.assertEqual(len(lst), 0)



t = testAVLList()
t.compare_with_list_by_in_order()