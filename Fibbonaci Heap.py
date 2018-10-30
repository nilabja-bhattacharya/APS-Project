import math
## Fib Heap
class FibHeap:
    def __init__(self):
        self.n = 0
        self.min = None
        self.root = []

## Fib Heap intenalTree
class Node:
    def __init__(self, val):
        self.degree = 0
        self.parent = None
        self.child = []
        self.mark = False
        self.key = val
        self.right = self

def makeNode():
    return Node()


def makeFibHeap():
    return FibHeap()

##Insert
def FibHeapInsert(h: FibHeap, node: Node):
    if(h.min == None):
        h.root = [node]
        h.min = node
    else:
        h.root.append(node)
        h.root[len(h.root)-2].right = node
        h.root[len(h.root)-1].right = h.root[0]
        if(node.key < h.min.key):
            h.min = node
    h.n = h.n + 1
#     print("printing root list")
#     for x in h.root:
#         print(x.key)

def D(n: int):
    #     print("log value = {0}".format(int(math.log2(n))+1))
    return int(math.log2(n))+1

def FibHeapLink(h: FibHeap, y, x):
    #     print("In link, root size {0}".format(len(h.root)))
    #     print("In link, x = {0}, y = {1}".format(x.key, y.key))
    h.root.remove(y)
    x.child.append(y)
    x.degree = x.degree+1
    y.mark = False
#     print("In link, abcd root size {0}".format(len(h.root)))


def consolidate(h: FibHeap):
    A = [None for i in range(0,D(h.n)+1)]
    #     print("In consolodate, root size {0}".format(len(h.root)))
    #     for w in h.root:
    #         print("Test consolodate, w= {0}".format(w.key))
    #         print("Test consolodate, w= {0}".format(w.degree))
    #     for i in range(0,len(h.root)):
    i = 0
    while(i < len(h.root)):
        #         print("In beginning i = {0}, root len {1}".format(i, len(h.root)))
        w = h.root[i]
        #         print("In consolodate, w= {0}".format(w.key))
        x = w
        d = x.degree
        #         print("x degree = {0}".format(x.degree))
        while not A[d] == None:
            #             print("In while x degree = {0}".format(x.degree))
            y = A[d]
            if x.key > y.key:
                temp = x
                x = y
                y = temp
            FibHeapLink(h, y, x)
            A[d] = None
            d = d+1
            i = i-1
        A[d] = x
        i = i+1
    for w in A:
        h.min = None
    for i in range(0, D(h.n)+1):
        if not A[i] == None:
            if h.min == None:
                h.root = [A[i]]
                h.min = A[i]
            else:
                h.root.append(A[i])
                if(A[i].key < h.min.key):
                    h.min = A[i]


##Extract min
def FibExtractMin(h: FibHeap):
    z = h.min
    if(not z == None):
        for x in z.child:
            h.root.append(x)
            x.parent = None
        h.root.remove(z)
        if(z == z.right):
            h.min = None
        else:
            h.min = z.right
            #             print("before consolodate {0}".format(h.min.key))
            #             print("before consolodate root size {0}".format(len(h.root)))
            consolidate(h)
        #             print("after consolodate root size {0}".format(len(h.root)))
        h.n = h.n - 1
    return z

def main():
    h = makeFibHeap()
    FibHeapInsert(h, Node(5))
    FibHeapInsert(h, Node(25))
    FibHeapInsert(h, Node(3))
    FibHeapInsert(h, Node(35))
    print(len(h.root))
    print(FibExtractMin(h).key)
    print(FibExtractMin(h).key)
    print(FibExtractMin(h).key)
    print(FibExtractMin(h).key)

if __name__ == '__main__':
    main()