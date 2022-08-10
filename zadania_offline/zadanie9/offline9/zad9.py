#Rafał Laskowski
'''
    Złożoność czasowa algorytmu: O(V^2 * E^2) - algorytm Edmondsa-Karpa pomnożony przez 2 razy liniowe przejścia
    Najpierw znajduje pierwsze ujście z najlepszym przepływem, potem na utworzonej sieci residualnej wykonuje drugi raz
    to samo i dodaje do siebie oba te wyniki.
'''

from zad9testy import runtests
from queue import Queue
from math import inf

def bfs(G, s, des, P): #G-graf, s-źródło, des-ujście, P-parents
    n = len(G)
    V = [False for _ in range(n)]
    V[s] = True
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in range(n):
            if G[u][v] > 0 and not V[v]:
                V[v] = True
                P[v] = u
                q.put(v)
                if v == des: #jeżeli dojdziemy do ujścia to kończymy szukanie ścieżki
                    return True
    return False

def max_flow_finder(G, graph, s, des, P): #graph-macierz sąsiedztwa, s-źródło, des-ujście, P-parents
    path = bfs(graph, s, des, P)
    v_to_del = -1
    result = 0
    while path:
        flow_cnt = inf
        x = des
        while x != s:
            if flow_cnt > graph[P[x]][x]:
                flow_cnt = graph[P[x]][x]
                v_to_del = x
            x = P[x]
        result += flow_cnt
        y = des
        while y != s:
            z = P[y]
            graph[z][y] -= flow_cnt
            graph[y][z] += flow_cnt
            y = P[y]
        path = bfs(graph, s, des, P)
    return result, v_to_del


def maxflow(G, s):
    n = len(G)  # ilość krawędzi NIE WIERZCHOŁKÓW
    il_ver = max(G, key=lambda K: K[1])[1]  # ilosć wierzchołków
    P = [-1 for i in range(il_ver + 1)]
    graph = [[-1 for _ in range(il_ver + 1)] for _ in range(il_ver + 1)]  # macierz sąsiedztwa
    for i in range(n):  # zamiana na macierz sąsiedztwa
        graph[G[i][0]][G[i][1]] = G[i][2]
    graph_to_copy = [x[:] for x in graph]
    to_return = 0
    v_to_del = -1
    maks = -1
    new_graph = graph
    for i in range(2):
        for j in range(il_ver+1):
            if j != s and j != v_to_del:
                tmp1, tmp2 = max_flow_finder(G, graph, s, j, P)
                if maks < tmp1:
                    maks = tmp1
                    v_to_del_tmp = tmp2
                    new_graph = [x[:] for x in graph]
            graph = [x[:] for x in graph_to_copy]
            P = [-1 for i in range(il_ver + 1)]
        to_return += maks
        graph = [x[:] for x in new_graph]
        graph_to_copy = [x[:] for x in new_graph]
        maks = -1
        v_to_del = v_to_del_tmp
    return to_return

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )