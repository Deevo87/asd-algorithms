# Rafał Laskowski
'''
Najpierw zamieniam liste krawędzie na liste sąsiedztwa, następnie dodaje tablice z wyznaczonymi wierzchołkami, w których
znajdują się anomalie. Algorytm wyszukiwania ścieżki działa następująco: jezeli napotkamy
pierwszy wierzcholek z anomalią, to dodajemy do jego opcji ścieżki rownież wszystkie inne anomalie.
'''

from zad5testy import runtests
from queue import PriorityQueue


def list_to_graph(E, n):
    G = [[] for i in range(n)]
    for v, u, x in E:
        G[v] += [(u, x)]
        G[u] += [(v, x)]
    return G


def Dijkstra(G, S, Sb, a, b):
    inf = 10 ** 20
    PQ = PriorityQueue()
    n = len(G)
    V = [False for i in range(n)]
    W = [inf for i in range(n)]
    W[a] = 0
    PQ.put((0, a))
    flag = True
    while not PQ.empty():
        _, v = PQ.get()
        if V[v]:
            continue
        V[v] = True
        for u, x in G[v]:
            if not V[u] and W[u] > W[v] + x:
                W[u] = W[v] + x
                PQ.put((W[u], u))
        if flag and Sb[v]:
            for u in S:
                if u != v:
                    W[u] = W[v]
                    PQ.put((W[u], u))
            flag = False
    if W[b] == inf:
        return None
    return W[b]


def spacetravel(n, E, S, a, b):
    G = list_to_graph(E, n)
    Sb = [False for i in range(n)]
    for i in S:
        Sb[i] = True
    w = Dijkstra(G, S, Sb, a, b)
    return w


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=False)
