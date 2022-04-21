from avl_skeleton import *
from printree import *


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
    

tester()