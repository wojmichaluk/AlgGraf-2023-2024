from lab4_4_testy import runtests
from LexBFS_and_graph_representation import *

def minimal_cover(V,L):
    G=[Node(i) for i in range(V)]
    for (u,v,_) in L:
        G[u-1].connect_to(v-1)
        G[v-1].connect_to(u-1)
    visited,RN,parents=LexBFS(G)
    visited.reverse()
    I=set()
    for v in visited:
        N=G[v].out
        if not I & N:
            I.add(v)
    return V-len(I)

runtests(minimal_cover)
