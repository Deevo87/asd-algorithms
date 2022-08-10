from zad9testy import runtests
from queue import Queue
from math import inf
from copy import deepcopy

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

def test(G, s):
    n = len(G)  # ilość krawędzi NIE WIERZCHOŁKÓW
    il_ver = max(G, key=lambda K: K[1])[1]  # ilosć wierzchołków
    P = [-1 for i in range(il_ver + 1)]
    graph = [[0 for _ in range(il_ver + 1)] for _ in range(il_ver + 1)]  # macierz sąsiedztwa
    for i in range(n):  # zamiana na macierz sąsiedztwa
        graph[G[i][0]][G[i][1]] = G[i][2]
    result = max_flow_finder(G, graph, s, 3, P)[0]
    return result

def maxflow(G, s):
    n = len(G)  # ilość krawędzi NIE WIERZCHOŁKÓW
    il_ver = max(G, key=lambda K: K[1])[1]  # ilosć wierzchołków
    P = [-1 for i in range(il_ver + 1)]
    flow = deepcopy(G)
    graph = [[-1 for _ in range(il_ver + 1)] for _ in range(il_ver + 1)]  # macierz sąsiedztwa
    for i in range(n):  # zamiana na macierz sąsiedztwa
        graph[G[i][0]][G[i][1]] = G[i][2]
    for i in range(il_ver+1):
        print(graph[i])
    print('/////////////////')
    graph_to_copy = deepcopy(graph)
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
                    new_graph = deepcopy(graph)
            graph = deepcopy(graph_to_copy)
            P = [-1 for i in range(il_ver + 1)]
        to_return += maks
        # for g in range(il_ver):
        #     print(graph[g])
        # print('//////////////////')
        graph = deepcopy(new_graph)
        graph_to_copy = deepcopy(new_graph)
        maks = -1
        v_to_del = v_to_del_tmp
    return to_return



if __name__ == '__main__':
    X = [(0, 1, 15), (1, 2, 2), (1, 3, 15), (1, 4, 3), (0, 2, 7), (0, 4, 6)]
    X2 = [(0, 1, 10), (1, 2, 2), (1, 3, 5), (1, 4, 3)]
    X1 = [(0, 1, 7), (0, 3, 3), (1, 3, 4), (1, 4, 6), (2, 0, 9), (2, 3, 7), (2, 5, 9), (3, 4, 9), (3, 6, 2), (5, 3, 3), (5, 6, 4), (6, 4, 8)]
    G = [(0, 1, 9), (0, 2, 9), (0, 3, 9), (1, 2, 2), (1, 3, 9), (1, 4, 7), (2, 4, 7), (3, 4, 7)]

    print(maxflow(G, 0))
    #print(test(X1, 2))

