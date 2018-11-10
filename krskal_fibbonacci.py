from Fibbonaci_Heap import *

V = None
E = None
EdgeList = []

class UnionFind:
    def __init__(self, N):
        self.rank = [0 for i in range(N+1)]
        self.p = [0 for i in range(N+1)]
        for i in range(N+1):
            self.p[i] = i

    def findSet(self, i: int):
        if (self.p[i] == i):
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self, i, j):
        if not self.isSameSet(i, j):
            x = self.findSet(i)
            y = self.findSet(j)
            if self.rank[x] > self.rank[y] :
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y] :
                    self.rank[y] += 1

def Kruskal(h: FibHeap):
    mst_cost = 0
    global EdgeList
    UF = UnionFind(V)
    for i in range(E):
        # x, y, z = EdgeList[i]
        temp = FibExtractMin(h)
        x = temp.key
        y = temp.x
        z = temp.y
        #print("In Kruskal {0}, {1}".format(y,z))
        if not UF.isSameSet(y, z):
            mst_cost += x
            UF.unionSet(y,z)
    return mst_cost

if __name__ == "__main__":
    # global V, E, EdgeList
    # V = 9

    # E = 14
    h = makeFibHeap()
    # # EdgeL = [(0,1,7),(0,3,6),(3,1,9),(3,2,8),(1,2,6)]
    # EdgeL = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    # for i in EdgeL:
    #     u, v, w = i
    #     print("edge: {0}, {1}, {2}".format(u,v,w))
    E = int(input())
    V = int(input())

    #V = 9
    #E = 14
    #h = vEB.of_size(32)
    # EdgeL = [(0,1,7),(0,3,6),(3,1,9),(3,2,8),(1,2,6)]
    #EdgeL = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    for i in range(E):
        u = int(input())
        v = int(input())
        w = int(input())
        FibHeapInsert(h, Node(w, u, v))
    print(Kruskal(h))
