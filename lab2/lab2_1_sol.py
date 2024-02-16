from lab2_1_testy import *
from queue import deque

def FordFulkerson(V,L,fun):
    G=[[0 for _ in range(V)] for _ in range(V)]
    for e in L:
        u,v,w=e
        G[u-1][v-1]=w
    flow=0
    path=BFS_or_DFS(G,0,V-1,fun)
    while path:
        w=cap(G,path)
        flow+=w
        update(G,path,w)
        path=BFS_or_DFS(G,0,V-1,fun)
    return flow

def BFS_or_DFS(G,s,t,fun):
    n=len(G)
    par=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    visited[s]=True
    q=deque()
    q.append(s)
    while q:
        if fun==0: v=q.popleft()
        else: v=q.pop()
        for i in range(n):
            if G[v][i]>0 and not visited[i]:
                par[i]=v
                visited[i]=True
                q.append(i)
        if visited[t]: break
    k=t
    path=[]
    while k!=None:
        path.append(k)
        k=par[k]
    if len(path)<2: return None
    path.reverse()
    return path

def cap(G,path):
    minf=G[path[0]][path[1]]
    for i in range(1,len(path)-1):
        minf=min(minf,G[path[i]][path[i+1]])
    return minf

def update(G,path,w):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]-=w
        G[path[i+1]][path[i]]+=w

#testy
runtests(FordFulkerson,0)
runtests(FordFulkerson,1)
