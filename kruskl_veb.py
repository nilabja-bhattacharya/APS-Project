from veb1 import *
from collections import defaultdict
V = None
E = None
EdgeList = []
nodes = defaultdict(list)
class edge:
    def __init__(self,u,v):
        self.u = u
        self.v = v
class UnionFind:
    def __init__(self, N):
        self.rank = [0 for i in range(N+1)]
        self.p = [0 for i in range(N+1)]
        for i in range(N+1):
            self.p[i] = i

    def findSet(self, i):
        if (self.p[i] == int(i)):
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
    time_start = time.clock()
    mst_cost = 0
    global EdgeList
    UF = UnionFind(V)
    for i in range(E):
        # x, y, z = EdgeList[i]
        #print(temp)
        temp = h.min()
        y=0
        z=0
        if nodes[temp]:
            tmp = nodes.get(temp)
            nodes.pop(temp,None)
            #print(tmp[0])
            #print(tmp)
            y = tmp[0].u
            z = tmp[0].v
            tmp.pop(0)
            #tmp.pop(0)
            #print (y)
            #print (z)
            if tmp:
                nodes[temp].extend(tmp)
            else:
                h.delete(temp)
        #print("In Kruskal {0}, {1}".format(x,y))
        if not UF.isSameSet(y, z):
            #print(mst_cost)
            mst_cost += temp
            UF.unionSet(y,z)
            #print(mst_cost)
            #print(temp)
    time_elapsed = (time.clock() - time_start)
    print("{0} {1} {2}".format(E,time_elapsed, mst_cost))
    return mst_cost





if __name__ == "__main__":
    # global V, E, EdgeList
    E = int(input())
    V = int(input())

    #V = 9
    #E = 14
    h = vEB.of_size(32)
    # EdgeL = [(0,1,7),(0,3,6),(3,1,9),(3,2,8),(1,2,6)]
    #EdgeList = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
    for i in range(E):
        u = int(input())
        v = int(input())
        w = int(input())
        #u,v,w = EdgeList[i]
        #print("edge: {0}, {1}, {2}".format(u,v,w))
        h.insert(w)
        # nodes[w].append(u)
        # nodes[w].append(v)
        nodes[w].append(edge(u,v))
        #print(nodes.get(w))
    #print(list(h))
    mst=kruskal(h)