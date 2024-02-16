from lab3_2_testy import runtests
from queue import PriorityQueue 

#struktura pomocnicza do przechowywania wierzchołku grafu
class Node:
    def __init__(self):
        self.edges={}
        self.merged=set()
        self.active=True

    def addEdge(self,to,weight):
        self.edges[to]=self.edges.get(to,0)+weight  
                                                    
    def delEdge(self, to):
        del self.edges[to]                             

def Stoer_Wagner(V,L):
    G=[Node() for i in range(V)]
    for (x,y,c) in L:
        G[x-1].addEdge(y-1,c)
        G[y-1].addEdge(x-1,c)
    n=len(G)
    result=float('inf')
    while n>1:
        potential_result=minimum_cut_phase(G)
        if potential_result<result:
            result=potential_result
        n-=1
    return result

def merge_vertices(G,x,y):
    v1=G[x]
    v2=G[y]
    merged=list(v2.merged)
    for vertex in merged:
        v1.merged.add(vertex)
    v2.active=False
    vertices=list(v2.edges.keys())
    for vertex in vertices:
        if vertex==x:
            v1.delEdge(y)
        else:
            weight=v2.edges.get(vertex)
            v1.addEdge(vertex,weight)
            G[vertex].addEdge(x,weight)
            G[vertex].delEdge(y)
        v2.delEdge(vertex)

def minimum_cut_phase(G):
    S=set()
    Q=PriorityQueue()
    n=len(G)    
    add_order=[]
    checked=[False for _ in range(n)]
    weight_sums=[0 for _ in range(n)]
    for i in range(n):
        if G[i].active:
            Q.put((0,i))
        else:
            checked[i]=True
            S.add(i)
    while len(S)<n:
        w_sum,v=Q.get()
        if not checked[v]:
            checked[v]=True
            S.add(v)
            add_order.append(v)
            for vertex in list(G[v].edges.keys()):
                if not checked[vertex]:
                    weight_sums[vertex]+=G[v].edges[vertex]
                    Q.put((-weight_sums[vertex],vertex))
    s=add_order[-1]
    t=add_order[-2]
    merge_vertices(G,s,t)
    return weight_sums[s] 

runtests(Stoer_Wagner)
