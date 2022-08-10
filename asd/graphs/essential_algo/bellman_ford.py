from math import inf

def Bellman_Ford(G, s): #G = [(początek, koniec, waga krawędzi), ...]
    n = len(G)
    max_ver = max(G, key=lambda z: z[1])[1]
    P = [-1 for _ in range(max_ver + 1)]
    D = [inf for _ in range(max_ver + 1)]
    D[s] = 0
    for v in range(len(G)-1):
        for p, q, w in G:
            if D[p] != inf and D[p] + w < D[q]:
                D[q] = D[p] + w
                P[q] = p
    # weryfikacja
    for x in G:
        u, v, w = x
        if D[u] != inf and D[u] + w < D[v]:
            return -1
    return P, D

if __name__ == '__main__':
    x =    [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    n = len(x)
    graph = []
    for i in range(n):
        for j in range(n):
            if x[i][j] != 0:
                graph.append((i, j, x[i][j]))
    print(graph)

    print(Bellman_Ford(graph, 0))