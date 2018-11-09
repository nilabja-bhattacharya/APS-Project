from collections import defaultdict
V = None
E = None
EdgeList = []
nodes = defaultdict(list)
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

def kruskal():
    mst_cost = 0
    global EdgeList
    UF = UnionFind(V)
    for i in range(E):
        x, y, z = EdgeList[i]
        #print("In Kruskal {0}, {1}".format(x,y))
        if not UF.isSameSet(y, z):
            #print(mst_cost)
            mst_cost += x
            UF.unionSet(y,z)
            #print(mst_cost)
            #print(i)
    return mst_cost


if __name__ == "__main__":
    E = int(input())
    V = int(input())

    for i in range(E):
        u = int(input())
        v = int(input())
        w = int(input())
        lst = []
        lst.append(w)
        lst.append(u)
        lst.append(v)
        EdgeList.append(lst)
    EdgeList.sort(key = lambda x: x[0])
    #print (EdgeList)
    print (kruskal())