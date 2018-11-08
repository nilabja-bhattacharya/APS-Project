from veb1 import *
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

def kruskal(h: vEB):
    mst_cost = 0
    global EdgeList
    UF = UnionFind(V)
    for i in range(E):
        # x, y, z = EdgeList[i]
        temp = h.min
        #print(temp)
        y=0
        z=0
        if nodes[temp]:
            tmp = nodes.get(temp)
            nodes.pop(temp,None)
            y = tmp[0]
            z = tmp[1]
            tmp.pop(0)
            tmp.pop(0)
            #print(tmp)
            #print (y)
            #print (z)
            if tmp:
                for j in range(len(tmp)):
                    nodes[temp].append(tmp[j])
            else:
                h.delete(temp)
        #print("In Kruskal {0}, {1}".format(x,y))
        if not UF.isSameSet(y, z):
            #print(mst_cost)
            mst_cost += temp
            UF.unionSet(y,z)
            #print(mst_cost)
            #print(i)
    return mst_cost



if __name__ == "__main__":
    # global V, E, EdgeList
    V = 9
    E = 14
    h = vEB.of_size(32)
    # EdgeL = [(0,1,7),(0,3,6),(3,1,9),(3,2,8),(1,2,6)]
    EdgeL = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    for i in EdgeL:
        u, v, w = i
        #print("edge: {0}, {1}, {2}".format(u,v,w))
        h.insert(w)
        nodes[w].append(u)
        nodes[w].append(v)
        #print(nodes.get(w))
    print(list(h))
    print(kruskal(h))