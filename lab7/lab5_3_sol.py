from lab5_3_testy import runtests
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort

def check_sat(V,F):
    G=build_implication_graph(V,F)
    SCC=strongly_connected_components(G)
    SCC_list=list(SCC)
    scc_count=0
    for S in SCC_list:
        current_component=set()
        for v in S:
            if -v in current_component:
                print("Formuła nie jest spełnialna.\n")
                return False
            current_component.add(v)
            G[v][0]['scc_component']=scc_count
        scc_count+=1
    print("Formuła jest spełnialna, wartościowanie:")
    H=build_connected_components_graph(G,SCC_list,scc_count)
    O=topological_sort(H)
    evaluation=find_literals_evaluation(G,SCC_list,O,V)
    show_evaluation(evaluation)
    print("Sprawdzam wartościowanie:",check_evaluation(evaluation,F),'\n')
    return True

def build_implication_graph(V,F):
    G=nx.DiGraph()
    G.add_edges_from([(i,0) for i in range(-V,V+1)])
    for u,v in F:
        G.add_edge(-u,v)
        G.add_edge(-v,u)
    return G

def build_connected_components_graph(G,SCC_list,n):
    H=nx.DiGraph()
    H.add_nodes_from([i for i in range(n)])
    for S in SCC_list:
        for v in S:
            for u in G[v]:
                if G[v][0]['scc_component']!=G[u][0]['scc_component']:
                    H.add_edge(G[v][0]['scc_component'],G[u][0]['scc_component'])
    return H

def find_literals_evaluation(G,SCC_list,O,V):
    evaluation={}
    for i in range(-V,V+1):
        evaluation[i]=None
    O_list=list(O)
    for scc in O_list:
        S=SCC_list[scc]
        for v in S:
            if evaluation[v]!=None:
                continue
            if evaluation[-v]!=None:
                evaluation[v]=not evaluation[-v]
            else:
                evaluation[v]=False
    evaluation_list=[]
    for i in range(1,V+1):
        evaluation_list.append(evaluation[i])
    return evaluation_list

def show_evaluation(evaluation):
    n=len(evaluation)
    for i in range(n):
        print("x_",i+1,": ",evaluation[i],sep='')
    print()

def check_evaluation(evaluation,F):
    def apply_evaluation(alternative):
        nonlocal evaluation
        l,r=alternative
        if l<0: left=not evaluation[-l-1]
        else: left=evaluation[l-1]
        if r<0: right=not evaluation[-r-1]
        else: right=evaluation[r-1]
        return left or right
    
    mapped_F=list(map(apply_evaluation,F))
    n=len(mapped_F)
    ev=True
    for i in range(n):
        ev = ev and mapped_F[i]
    return ev

runtests(check_sat)
