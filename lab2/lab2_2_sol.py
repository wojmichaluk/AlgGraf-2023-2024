from lab2_2_testy import *
from queue import deque

def FordFulkerson(V,L,fun):
    Gr=[[0 for _ in range(V)] for _ in range(V)]
    for e in L:
        u,v,w=e
        Gr[u-1][v-1]=w
        Gr[v-1][u-1]=w
    min_flow=float('inf')
    for i in range(V-1):
        for j in range(i+1,V):
            G=[[Gr[k][l] for l in range(V)] for k in range(V)]
            flow=0
            path=BFS_or_DFS(G,i,j,fun)
            while path:
                flow+=1
                update(G,path)
                path=BFS_or_DFS(G,i,j,fun)
        min_flow=min(flow,min_flow)
    return min_flow

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

def update(G,path):
    for i in range(len(path)-1):
        G[path[i]][path[i+1]]=0
        G[path[i+1]][path[i]]=0

#testy
runtests(FordFulkerson,0)
runtests(FordFulkerson,1)
