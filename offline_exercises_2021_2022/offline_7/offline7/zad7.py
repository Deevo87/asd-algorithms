from zad7testy import runtests


def DFS_visit(G, u, visited, P, t, gate):  # False - północna brama, True - prawa brama
    t += 1
    visited[u][0], visited[u][1] = True, True
    if gate:  # wchodzimy przez południową bramę
        gate = False
        x = 1
    else:  # wchodzimy przez południową bramę
        gate = True
        x = 0
    for v in G[u][x]:
        if not visited[v][abs(x - 1)]:
            print(G[v][x])
            P[v] = u
            DFS_visit(G, v, visited, P, t, gate)
        t += 1

#def DFS(G):
def droga(G):
    n = len(G)
    visited = [[False, False] for _ in range(n)]
    t = 0
    odp = [0 for _ in range(n)]
    for u in range(n):
        if not visited[u][0] and not visited[u][1]:
            gate = False
            DFS_visit(G, u, visited, odp, t, gate)
    print(odp)
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=False)
