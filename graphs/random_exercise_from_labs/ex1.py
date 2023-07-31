# Zadanie 1. (sciezka Hamiltona w DAGu) Sciezka Hamiltona to sciezka przechodzaca przez wszystkie
# wierzchołki w grafie, przez kazdy dokładnie raz. W ogólnym grafie znalezienie sciezki Hamiltona jest problemem
# NP-trudnym. Prosze podac algorytm, który stwierdzi czy istnieje sciezka Hamiltona w acyklicznym
# grafie skierowanym.

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

def hamilton(G): # True jak ma ścieżkę hamiltona, Flase jak nie ma
    n = len(G)
    flag = False
    sor_G = topological_sort(G)
    for v in range(len(sor_G)):
        for u in G[sor_G[v]]:
            if v + 1 < len(sor_G) and sor_G[v+1] == u:
                flag = True
                break
        if not flag:
            return False
        flag = False
    #dopisz czy ma sąsiadów


if __name__ == '__main__':
    graph = [[1, 2, 5], [2, 4], [None], [None], [3, 5, 6], [None], [None]]
    print(topological_sort(graph))
    print(hamilton(graph))
