#Wojciech Michaluk
#Program składa się z dwóch głównych etapów: najpierw
#otrzymane dane wejściowe przepisuję na graf (drzewo),
#wykorzystując pomocniczą klasę Vertex, natomiast same
#krawędzie dodatkowo zapisuję w słowniku, wykorzystując
#pomocniczą klasę Edge. Pomijam przy tym krawędzie, w których
#jednym z końców jest wejście do grobowca - jako że i tak nie
#może się ono (jako wierzchołek) znaleźć na potencjalnej trasie.
#Następnie próbuję znaleźć drogę opisaną na papirusie,
#korzystając z funkcji DFS (nie jest to stricte algorytm DFS, ale
#działa ona na podobnej zasadzie - przeszukuje "w głąb").
#Jeżeli uda się znaleźć trasę pasującą do opisanej (zgodnie
#z przyjętym rozumieniem oznaczeń na papirusie), to program
#zwraca wynik True, w przeciwnym razie False. Aby stwierdzić,
#czy trasa istnieje, algorytm sprawdza wszystkie możliwości,
#tzn. rozważa potencjalny start w każdym wierzchołku i bada,
#czy uda się przejść całą trasę. Ze względu na to i sposób
#działania funkcji DFS, niestety złożoność czasowa algorytmu
#jest wysokiego rzędu - nie jestem w stanie jej dokładnie podać;
#celowałem w O(np), gdzie n - liczba wierzchołków, p - długość
#trasy, wykorzystując programowanie dynamiczne, ale nie udało
#mi się dojść do w pełni poprawnego programu. Złożoność
#pamięciową programu szacuję na O(p) ze względu na wywołania
#rekurencyjne DFS, ale mogę się mylić.

from data import runtests

#główna funkcja
def solve(N, entrance, corridors, path):
    G=[Vertex() for i in range(N)]
    E={}
    for edge in corridors:
        u,v=edge[0]-1,edge[1]-1
        if u!=entrance-1 and v!=entrance-1:
            G[u].neighbours.append(v)
            G[v].neighbours.append(u)
            E[(u,v)]=Edge()
            E[(v,u)]=Edge()
    p=path.split(" ")
    for v in range(N):
        if DFS(G,E,v,p):
            return True
    return False

#pomocnicze klasy dla wierzchołka i krawędzi
class Vertex:
    def __init__(self):
        self.neighbours=[]
        self.visited_before=0

class Edge:
    def __init__(self):
        self.visited=False
        self.count=None

#pomocnicze funkcje
def DFS(G,E,v,p,idx=0):
    if idx==len(p):
        return True
    c=p[idx]
    if c=='+':
        for u in G[v].neighbours:
            if pass_edge(G,E,u,v):
                if DFS(G,E,u,p,idx+1):
                    return True
                reset_edge(G,E,u,v)
    elif c=='^':
        for u in G[v].neighbours:
            if E[(u,v)].visited:
                if DFS(G,E,u,p,idx+1):
                    return True
    else:
        for u in G[v].neighbours:
            if E[(v,u)].visited and E[(v,u)].count==int(c):
                if DFS(G,E,u,p,idx+1):
                    return True
    return False

def pass_edge(G,E,u,v):
    curr_edge=E[(v,u)]
    alt_edge=E[(u,v)]
    if not curr_edge.visited and not alt_edge.visited:
        G[v].visited_before+=1
        curr_edge.visited=True
        curr_edge.count=G[v].visited_before
        return True
    return False

def reset_edge(G,E,u,v):
    curr_edge=E[(v,u)]
    G[v].visited_before-=1
    curr_edge.visited=False

runtests(solve)
