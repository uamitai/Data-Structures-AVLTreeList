from avl_skeleton import *
from printree import *

def tester():
    T1 = AVLTreeList()
    for i in range(2):
        T1.append(i)
    T1.delete(0)
    print(printree(T1))

tester()