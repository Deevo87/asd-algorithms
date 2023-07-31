# Edmonds-Karp Algorithm
from math import inf
def max_flow(C, s, t):
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)
    #  print path
    while path != None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    return sum(F[s][i] for i in range(n))


# find path by using BFS
def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                print(paths)
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


# make a capacity graph
# node   0   1   2   3   4   t
C =  [[ 0, 7, 0, 3, 0, 0, 0],  # s
     [ 0, 0, 0, 4, 6, 0, 0],  # o
     [ 0, 0, 0, 7, 0, 9, 0],  # p
     [ 0, 0, 0, 0, 9, 0, 2],  # q
     [ 0, 0, 0, 0, 0, 0, 0],  # r
     [ 0, 0, 0, 3, 0, 0, 4],
     [ 0, 0, 0, 0, 8, 0, 0]]# t

n = len(C)
max_flow_value = -inf
for i in range(n):
    source = i  # A
    for j in range(n):
        sink = j  # F
        if source != sink:
            max_flow_value = max(max_flow_value, max_flow(C, source, sink))
print("Edmonds-Karp algorithm")
print("max_flow_value is: ", max_flow_value)