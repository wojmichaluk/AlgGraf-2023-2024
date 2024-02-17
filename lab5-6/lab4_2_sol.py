from lab4_2_testy import runtests
from LexBFS_and_graph_representation import *

def find_max_clique(V,L):
    G=[Node(i) for i in range(V)]
    for (u,v,_) in L:
        G[u-1].connect_to(v-1)
        G[v-1].connect_to(u-1)
    visited,RN,parents=LexBFS(G)
    max_clique=1
    for i in range(V):
        if len(RN[i])+1>max_clique:
            max_clique=len(RN[i])+1
    return max_clique

runtests(find_max_clique)
