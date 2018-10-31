V = None
E = None
EdgeList = []

class UnionFind:
    def __init__(self, N):
        self.rank = [0 for i in range(N)]
        self.p = [0 for i in range(N)]
        for i in range(N):
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

def Kruskal():
    mst_cost = 0
    global EdgeList
    UF = UnionFind(V)
    for i in range(E):
        x, y, z = EdgeList[i]
        print("In Kruskal {0}, {1}".format(y,z))
        if not UF.isSameSet(y, z):
            mst_cost += x
            UF.unionSet(y,z)
    return mst_cost

def main():
    global V, E, EdgeList
    V = 4
    E = 5
    # V = int(input())
    # E = int(input())
    EdgeL = [(0,1,7),(0,3,6),(3,1,9),(3,2,8),(1,2,6)]
    for i in EdgeL:
        u, v, w = i
        print("edge: {0}, {1}, {2}".format(u,v,w))
        # v = int(input())
        # w = int(input())
        EdgeList.append((w,u,v))
    EdgeList.sort()
    print(Kruskal())

if __name__ == "__main__":
    main()

    g.addEdge(0, 1, 4);
    g.addEdge(0, 7, 8);
    g.addEdge(1, 2, 8);
    g.addEdge(1, 7, 11);
    g.addEdge(2, 3, 7);
    g.addEdge(2, 8, 2);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 4, 9);
    g.addEdge(3, 5, 14);
    g.addEdge(4, 5, 10);
    g.addEdge(5, 6, 2);
    g.addEdge(6, 7, 1);
    g.addEdge(6, 8, 6);
    g.addEdge(7, 8, 7);