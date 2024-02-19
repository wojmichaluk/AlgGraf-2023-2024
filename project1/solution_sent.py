#Wojciech Michaluk
#Program składa się z kilku etapów: najpierw otrzymane dane wejściowe
#przepisuję, wykorzystując pomocniczą klasę Vertex. Następnie znajduję
#punkty artykulacji, korzystając z algorytmu DFS (uwaga: niestety dla pewnych
#klas grafów algorytm iteracyjny nie działa poprawnie, ale późniejsze funkcje
#obliczają oczekiwany wynik prawidłowo). Na podstawie punktów artykulacji
#wyznaczam składowe w "nowym" grafie - punkty artykulacji stają się
#samodzielnymi wierzchołkami, a połączone "zwykłe" wierzchołki skupiają się
#w jeden wierzchołek. Następnie szukam najlepszej ścieżki, tzn. takiej, że
#przejdziemy pod największą liczbą łuków triumfalnych, zachowując możliwie
#najmniejszy łączny czas. Potencjalnym startowym wierzchołkiem jest dowolny
#wierzchołek, który jest w nowym grafie w wierzchołku mającego jednego sąsiada
#("odosobnionym"; tutaj również uwaga - jeżeli punkty artykulacji są źle
#wyznaczone, to ten startowy wierzchołek również jest niepoprawnie wybierany,
#choć zwracane wyniki są poprawne (?), nie licząc dwóch testów - dla których
#z kolei punkty artykulacji są znajdowane poprawnie, ale czas przejścia jest liczony
#niepoprawnie). Przechodzę algorytmem Dijkstry dwukrotnie - za pierwszym razem
#startuję z wierzchołka wskazanego powyżej, dla niego jest pewien "najlepszy"
#wierzchołek, który będzie punktem wyjścia dla drugiego przejścia. Liczbę łuków
#triumfalnych przy przejściu przez punkt artykulacji zwiększam tylko wtedy, gdy jest
#to jedyny punkt łączący poprzedni wierzchołek z właśnie sprawdzanym potencjalnym
#następnym wierzchołkiem (czyli gdy nie ma cyklu). Uwaga: algorytm Dijkstry
#przechodzi po oryginalnym grafie, natomiast cykl sprawdzam w nowym grafie.
#Ze względu na każdorazowe sprawdzanie cyklu (algorytmem DFS) złożoność czasowa
#algorytmu jest nienajlepsza - O(E(V+E)). Komentarze w dalszej części programu są po
#angielsku, aczkolwiek są autorskie - program jest napisany samodzielnie.

from data import runtests
from queue import PriorityQueue
import sys
sys.setrecursionlimit(100000)

#main function
def solve(N,streets):
    G=[Vertex([i]) for i in range(N)]
    for a,b,t in streets:
        G[a-1].neighbours[b-1]=t
        G[b-1].neighbours[a-1]=t
    articulation_points=find_articulation_points(G)
    new_graph=build_new_graph(G,articulation_points)
    arches,time=find_best_path(G,new_graph,articulation_points)
    return (arches,time)

#helpful graph vertex representation
class Vertex:
    def __init__(self,v=None):
        self.vertices=v #vertices contained (in original graph it is just one vertex)
        self.index=None #index in new graph (used only for vertices in old graph)
        self.neighbours={} #dictionary of neighbours (keys) and edge weight (values)

#auxiliary functions 
def find_articulation_points(G):
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    children=[[] for _ in range(n)]
    times=[None for _ in range(n)]
    low=[None for _ in range(n)]
    time=[0] #so that reference is passed
    articulation_points=set()
    DFSVisit(G,0,visited,parent,children,times,low,time)
    if len(children[0])>1:
        articulation_points.add(0)
    for i in range(1,n):
        for v in children[i]:
            if low[v]>=times[i]:
                articulation_points.add(i)
                break
    return articulation_points

def DFSVisit(G,u,visited,parent,children,times,low,time):
    n=len(G)
    add_order=[]
    anc=[[] for _ in range(n)]
    desc=[[] for _ in range(n)]
    visited[0]=True
    times[0]=time[0]
    stack=[0]
    while stack:
        u=stack.pop()
        add_order.append(u)
        for v in G[u].neighbours.keys():
            if not visited[v]:
                visited[v]=True
                time[0]+=1
                desc[u].append(v)
                parent[v]=u
                children[u].append(v)
                times[v]=time[0]
                stack.append(v)
            elif v!=parent[u]:
                anc[u].append(v)
    for j in range(n-1,-1,-1):
        v=add_order[j]
        min_u=n+1
        for i in range(len(anc[v])):
            if times[anc[v][i]]<min_u:
                min_u=times[anc[v][i]]
        min_w=n+1
        for i in range(len(desc[v])):
            if low[desc[v][i]]<min_w:
                min_w=low[desc[v][i]]
        low[v]=min(times[v],min_u,min_w)

def build_new_graph(G,articulation_points):
    n=len(G)
    visited=[False for _ in range(n)]
    temp_vertices=[]
    for p in articulation_points:
        visited[p]=True
        G[p].index=len(temp_vertices)
        temp_vertices.append([[p],set()])
    for p in articulation_points:
        for v in G[p].neighbours.keys():
            if v in articulation_points:
                temp_vertices[G[p].index][1].add(G[v].index)
    for i in range(n):
        if not visited[i]:
            temp_vertices.append([[],set()])
            set_normal_vertex(G,i,visited,articulation_points,temp_vertices)
    m=len(temp_vertices)
    Gr=[Vertex() for _ in range(m)]
    for i in range(m):
        Gr[i].vertices=temp_vertices[i][0]
        for v in temp_vertices[i][1]:
            Gr[i].neighbours[v]=1 #default value, as it is not needed in this graph
    return Gr

def set_normal_vertex(G,i,visited,articulation_points,temp_vertices):
    visited[i]=True
    stack=[i]
    while stack:
        u=stack.pop()
        temp_vertices[-1][0].append(u)
        G[u].index=len(temp_vertices)-1
        for v in G[u].neighbours.keys():
            if not visited[v]:
                visited[v]=True
                stack.append(v)
            elif v in articulation_points and G[v].index not in temp_vertices[-1][1]:
                index=G[v].index
                temp_vertices[-1][1].add(index)
                temp_vertices[index][1].add(G[u].index)

def find_best_path(G,Gr,articulation_points):
    n=len(G)
    for i in range(n):
        if len(Gr[G[i].index].neighbours.keys())==1:
            potential_start_vertex=i
            break
    start,arches,time=dijkstra(G,Gr,potential_start_vertex,articulation_points)
    v,arches,time=dijkstra(G,Gr,start,articulation_points)
    return arches,time

def dijkstra(G,Gr,start,articulation_points):
    n=len(G)
    times=[float('inf') for _ in range(n)]
    times[start]=0
    arches=[0 for _ in range(n)]
    used_edges=[set() for _ in range(n)]
    q=PriorityQueue()
    q.put((0,0,start,None))
    while not q.empty():
        a,t,u,p=q.get()
        a*=-1
        if a==arches[u] and t==times[u]:
            if u in articulation_points and p is not None:
                for v in G[u].neighbours.keys():
                    if v not in used_edges[u]:
                        c=G[u].neighbours[v]
                        cycle=is_cycle(Gr,G[p].index,G[u].index,G[v].index)
                        if cycle and relax(times,arches,v,c,u,0):
                            q.put((-arches[u],times[u]+c,v,u))
                            used_edges[u].add(v)
                            used_edges[v].add(u)
                        elif not cycle and relax(times,arches,v,c,u,1):
                            q.put((-arches[u]-1,times[u]+c,v,u))
                            used_edges[u].add(v)
                            used_edges[v].add(u)
            else:
                for v in G[u].neighbours.keys():
                    if v!=p and v not in used_edges[u]:
                        c=G[u].neighbours[v]
                        if relax(times,arches,v,c,u,0):
                            q.put((-arches[u],times[u]+c,v,u))
                            used_edges[u].add(v)
                            used_edges[v].add(u)
    most_arches=arches[0]
    best_time=times[0]
    best_v=0
    for i in range(1,n):
        if arches[i]>most_arches:
            most_arches=arches[i]
            best_time=times[i]
            best_v=i
        elif arches[i]==most_arches and times[i]<best_time:
            best_time=times[i]
            best_v=i
    return best_v,most_arches,best_time

def relax(times,arches,v,c,u,a):
    if arches[v]<arches[u]+a:
        arches[v]=arches[u]+a
        times[v]=times[u]+c
        return True
    elif arches[v]==arches[u]+a and times[v]>times[u]+c:
        times[v]=times[u]+c
        return True
    return False

def is_cycle(Gr,p,u,v):
    n=len(Gr)
    visited=[False for _ in range(n)]
    visited[u]=True
    cycle_exists=check_cycle(Gr,visited,p,v)
    return cycle_exists

def check_cycle(Gr,visited,p,v):
    if p==v:
        return True
    visited[p]=True
    for neighbour in Gr[p].neighbours.keys():
        if not visited[neighbour]:
            result=check_cycle(Gr,visited,neighbour,v)
            if result:
                return result
    return False

runtests(solve)