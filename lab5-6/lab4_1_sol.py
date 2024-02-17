from lab4_1_testy import runtests
from LexBFS_and_graph_representation import *

def is_chordal(V,L):
    G=[Node(i) for i in range(V)]
    for (u,v,_) in L:
        G[u-1].connect_to(v-1)
        G[v-1].connect_to(u-1)
    visited,RN,parents=LexBFS(G)
    for i in range(V):
        if parents[i] is not None:
            if not (RN[i]-set([parents[i]])) <= RN[parents[i]]:
                return False
    return True

runtests(is_chordal)
