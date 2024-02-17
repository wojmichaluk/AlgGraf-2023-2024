from lab4_3_testy import runtests
from LexBFS_and_graph_representation import *

def chromatic_number(V,L):
    G=[Node(i) for i in range(V)]
    for (u,v,_) in L:
        G[u-1].connect_to(v-1)
        G[v-1].connect_to(u-1)
    visited,RN,parents=LexBFS(G)
    color=[0 for _ in range(V)]
    for v in visited:
        N=G[v].out
        used={color[u] for u in N}
        c=1
        while c in used:
            c+=1
        color[v]=c
    return max(color)

runtests(chromatic_number)
