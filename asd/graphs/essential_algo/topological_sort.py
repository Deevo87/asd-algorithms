def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    S = []
    P = [None for _ in range(n)]
    time = 0
    for u in range(n):
        if not visited[u]:
            DFS_visit(G, u, time, visited, P, S)
    return S

def DFS_visit(G, u, time, visited, P, S):
    time += 1
    visited[u] = True
    for v in G[u]:
        if v is not None and not visited[v]:
            P[v] = u
            DFS_visit(G, v, time, visited, P, S)
    S.insert(0, u)

