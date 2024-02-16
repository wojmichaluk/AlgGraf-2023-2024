from lab1_testy import *
from queue import deque
from queue import PriorityQueue

#wersja 1
def tourist_guide_v1(V,L,s,t):
    L.sort(key=lambda x: x[2],reverse=True)
    return find_val(V,L,s,t)

class Node:
    def __init__(self,value):
        self.parent=self
        self.rank=0
        self.value=value

def findset(x):
    if x.parent!=x:
        x.parent=findset(x.parent)
    return x.parent

def union(x,y):
    x=findset(x)
    y=findset(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1

def find_val(V,L,s,t):
    N=[Node(i) for i in range(V)]
    for e in L:
        u,v,w=e
        if findset(N[u-1])!=findset(N[v-1]):
            union(N[u-1],N[v-1])
            return_val=w
        if findset(N[s])==findset(N[t]):
            return return_val

#------------------------------------------#

#wersja 2       
def tourist_guide_v2(V,L,s,t,fun):
    G=[[] for i in range(V)]
    min_c=max_c=L[0][2]
    for u,v,c in L:
        u-=1
        v-=1
        if c<min_c: min_c=c
        elif c>max_c: max_c=c
        G[u].append((v,c))
        G[v].append((u,c))
    res=min_c
    while min_c<=max_c:
        lim=min_c+(max_c-min_c)//2
        found=BFS_or_DFS(G,s,t,lim,fun)
        if found:
            res=lim
            min_c=lim+1
        else:
            max_c=lim-1
    return res
        
def BFS_or_DFS(G,s,t,lim,fun):
    n=len(G)
    visited=[False for _ in range(n)]
    visited[s]=True
    q=deque()
    q.append(s)
    while q:
        if fun==1: v=q.popleft()
        else: v=q.pop()
        for u,c in G[v]:
            if not visited[u] and c>=lim:
                visited[u]=True
                q.append(u)
        if visited[t]: return True
    return False

#------------------------------------------#

#wersja 3
def tourist_guide_v3(V,L,s,t):
    G=[[] for i in range(V)]
    for u,v,c in L: 
        u-=1
        v-=1
        G[u].append((v,c))
        G[v].append((u,c))
    return alt_dijkstra(G,s,t)

def alt_dijkstra(G,s,t):
    n=len(G)
    min_val=float('inf')
    visited=[False for _ in range(n)]
    Q=PriorityQueue()
    Q.put((-float('inf'),s))
    while not Q.empty():
        w,u=Q.get()
        visited[u]=True
        w*=-1
        min_val=min(min_val,w)
        if visited[t]: break
        for v,c in G[u]:
            if not visited[v]:
                Q.put((-c,v))
    return min_val

#------------------------------------------#

runtests(tourist_guide_v1,0)
runtests(tourist_guide_v2,1)
runtests(tourist_guide_v2,2)
runtests(tourist_guide_v3,3)
