#include <bits/stdc++.h>

using namespace std;
typedef pair<int,int> ii;
typedef vector<int> vi;
vector< pair<int, ii> > EdgeList;
int V,E;
class UnionFind {
private: vi p, rank;
public:
    UnionFind(int N) { 
        rank.assign(N, 0);
        p.assign(N, 0); 
        for (int i = 0; i < N; i++) p[i] = i; 
    }
    int findSet(int i){ 
        return (p[i] == i) ? i : (p[i] = findSet(p[i])); 
    }
    bool isSameSet(int i, int j) { 
        return findSet(i) == findSet(j); 
    }
    void unionSet(int i, int j) {
        if (!isSameSet(i, j)) {
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) p[y] = x;
            else {
                p[x] = y;
                if (rank[x] == rank[y]) rank[y]++; 
            }
        } 
    } 
};

int Kruskal(){
    int mst_cost = 0;
    UnionFind UF(V);
    for (int i = 0; i < E; i++) {
        pair<int, ii> front = EdgeList[i];
        if (!UF.isSameSet(front.second.first, front.second.second)) {
            mst_cost += front.first;
            UF.unionSet(front.second.first, front.second.second);
        } 
    }
    return mst_cost;
}

int main(){
    cin>>V>>E;
    int u,v,w;
    for (int i = 0; i < E; i++) {
        scanf("%d %d %d", &u, &v, &w);
        EdgeList.push_back(make_pair(w, ii(u, v)));
    }
    sort(EdgeList.begin(), EdgeList.end());
    cout<<Kruskal()<<endl;
    return 0;
}