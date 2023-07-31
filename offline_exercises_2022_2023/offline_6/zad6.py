#Rafał Laskowski

'''
Stworzyłem jedno dużo źródło i ujście oraz graf z krawędziami o wagach 1 i użyłem forda fulkersona do obliczenia
max flowa.
'''

from zad6testy import runtests
from collections import deque


def dfs(S, T, matrix, Nodes):
    n = len(S)
    m = len(T)
    N = len(Nodes)
    Q = deque()
    Visited = [-1 for i in range(N)]

    for i in range(n):
        if S[i]:
            Q.append((i, N))
    while Q:
        v, parent = Q.pop()

        if Visited[v] != -1:
            continue
        Visited[v] = parent
        if v >= n:
            if not T[v - n]:
                return Visited, v
            for u in Nodes[v]:
                flow = 1 - matrix[u][v - n]
                if Visited[u] == -1 and flow:
                    Q.append((u, v))
        else:
            for u in Nodes[v]:
                flow = matrix[v][u - n]
                if Visited[u] == -1 and flow:
                    Q.append((u, v))
    return False, False


def binworker(M):
    n = len(M)
    S = [1 for _ in range(n)]
    m = max([max(i) for i in M]) + 1
    T = [0 for _ in range(m)]
    N = n + m
    Nodes = [[] for i in range(n + m)]
    for worker in range(n):
        for machine in M[worker]:
            Nodes[worker].append(machine + n)
            Nodes[n + machine].append(worker)
    matrix = [[0 for i in range(m)] for j in range(n)]
    for v in range(n):
        for u in M[v]:
            matrix[v][u] = 1
    Visited, v = dfs(S, T, matrix, Nodes)
    while Visited:
        parent = Visited[v]
        T[v - n] = 1
        while parent != N:
            if v >= n:
                matrix[parent][v - n] = 0
            else:
                matrix[v][parent - n] = 1
            v = parent
            parent = Visited[parent]
        S[v] = 0
        Visited, v = dfs(S, T, matrix, Nodes)
    return sum(T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
