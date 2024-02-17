from lab5_1_testy import runtests
import networkx as nx
from networkx.algorithms.planarity import check_planarity

def is_planar(V,L):
    G=nx.Graph()
    for (u,v,_) in L:
        G.add_edge(u-1,v-1)
    return check_planarity(G)[0]

runtests(is_planar)
