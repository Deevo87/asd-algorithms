from queue import PriorityQueue
from math import inf
import networkx as nx


def prim(G, s):
    n = len(G)
    q = PriorityQueue()
    visited = [False for _ in range(n)]
    D = [inf for _ in range(n)]
    Parent = [i for i in range(n)]
    D[s] = 0
    q.put((D[s], s))
    while not q.empty():
        u = q.get()[1]
        for v in range(n):
            if G[u][v] > 0 and not visited[v] and D[v] > G[u][v]:
                D[v] = G[u][v]
                Parent[v] = u
                q.put((D[v], v))
        visited[u] = True
    return Parent, D


def prim_tab(G, s):
    n = len(G)
    q = PriorityQueue()
    visited = [False for _ in range(n)]
    D = [inf for _ in range(n)]
    P = [i for i in range(n)]
    D[s] = 0
    q.put((D[s], s))
    while not q.empty():
        u = q.get()[1]
        for v in G[u]:
            if not visited[v[1]] and D[v[1]] > v[0]:
                P[v[1]] = u
                D[v[1]] = v[0]
                q.put(v)
        visited[u] = True
    return P


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
    g = [[]for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
                if x[i][j] != 0:
                    g[i].append((x[i][j], j))
    print(g)
    print(prim(x, 0))
    print(prim_tab(g, 0))