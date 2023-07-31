# Proszę zaimplementować algorytm sprawdzający czy graf jest dwudzielny (czyli zauważyć, że to
# 2-kolorowanie i użyć DFS lub BFS).
from queue import Queue

def bipartite_graph(G, start):
    n = len(G)
    q = Queue()
    q.put(start)
    parent = [-1 for _ in range(n)]
    D = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[start] = True
    D[start] = 0
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                D[v] = D[u] + 1
                visited[v] = True
                q.put(v)
            else:
                if D[v] % 2 == D[u] % 2:
                    return False
    print(D)
    return True



if __name__ == '__main__':
    graph = [[2, 3, 4, 5, 7], [2, 3, 4, 7], [0, 1, 6, 8], [0, 1], [0, 1, 6], [0, 6], [2, 4, 5, 7], [0, 1, 6], [2, 9], [8, 10], [9]]
    print(bipartite_graph(graph, 0))