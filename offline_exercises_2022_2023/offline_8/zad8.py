# Rafał Laskowski
"""
    Generalnie mechanizm jest prosty funkcją przypominającą BST scalam plamy w jedno pole i towrzę z tego liniową tablice.
    Następnie dopóki mam opcje w kolejce lub nie starcza mi paliwa na dojsćie do docelowaego pola szukam najlpeszego
    wyniku zliczając przy tym liczbę tankowań.
    O(n*m)
"""

from zad8testy import runtests
from collections import deque
from heapq import heappush, heappop


def BFS(T, Visited, start_u, start_v):
    suma = 0
    Q = deque()
    Q.append((start_u, start_v))
    while Q:
        u, v = Q.popleft()
        if Visited[u][v]:
            continue
        Visited[u][v] = True
        suma += T[u][v]
        for off in [-1, 1]:
            if len(T[0]) > v + off >= 0 and not Visited[u][v + off] and T[u][v + off] != 0:
                Q.append((u, v + off))
            if 0 <= u + off < len(T) and not Visited[u + off][v] and T[u + off][v] != 0:
                Q.append((u + off, v))
    return suma


def plan(T):
    m = len(T[0])
    n = len(T)
    Visited = [[False for _ in range(m)] for _ in range(n)]
    Linear = [0 for i in range(m)]
    for v in range(m):
        if T[0][v] != 0 and not Visited[0][v]:
            Linear[v] = BFS(T, Visited, 0, v)
    i = 0
    tanked = 0
    Q = [-Linear[0]]
    while Q:
        fuel = -heappop(Q)
        tanked += 1
        if i + fuel >= m - 1:
            break
        else:
            for j in range(i + 1, i + fuel + 1):
                heappush(Q, -Linear[j])
            i += fuel
    else:
        return -1
    return tanked


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
