from queue import deque

#graph representation
class Node:
    def __init__(self,idx):
        self.idx=idx
        self.out=set()

    def connect_to(self,v):
        self.out.add(v)

def LexBFS(G):
    n=len(G)
    visited=[]
    predecessors={}
    parents=[None for _ in range(n)]
    for i in range(n):
        predecessors[i]=set()
    starting_set=set([i for i in range(1,n)])
    to_be_visited=deque([starting_set,set([0])])
    while len(visited)<n:
        visited_vertex=to_be_visited[-1].pop()
        if not to_be_visited[-1]:
            to_be_visited.pop()
        visited.append(visited_vertex)
        new_to_be_visited=deque()
        for i in range(len(to_be_visited)-1,-1,-1):
            Y=set()
            for v in to_be_visited[i]:
                if visited_vertex in G[v].out:
                    predecessors[v].add(visited_vertex)
                    parents[v]=visited_vertex
                    Y.add(v)
            to_be_visited[i]-=Y
            if Y:
                new_to_be_visited.appendleft(Y)
            if to_be_visited[i]:
                new_to_be_visited.appendleft(to_be_visited[i])
        to_be_visited=new_to_be_visited
    return visited,predecessors,parents

def checkLexBFS(G,vs):
    n = len(G)
    pi=[None]*n
    for i,v in enumerate(vs):
        pi[v]=i
    for i in range(n-1):
        for j in range(i+1,n-1):
            Ni=G[vs[i]].out
            Nj=G[vs[j]].out
            verts=[pi[v] for v in Nj-Ni if pi[v]<i]
            if verts:
                viable=[pi[v] for v in Ni-Nj]
                if not viable or min(verts)<=min(viable):
                    return False
    return True
