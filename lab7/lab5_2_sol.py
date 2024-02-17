from lab5_2_testy import runtests
import networkx as nx
from networkx.algorithms.flow import maximum_flow

def find_max_flow(V,L):
    G=nx.DiGraph()
    for (u,v,w) in L:
        G.add_edge(u-1,v-1,capacity=w)
    return maximum_flow(G,0,V-1)[0]

runtests(find_max_flow)
