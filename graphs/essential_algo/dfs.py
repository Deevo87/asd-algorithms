def DFS(G, n):
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    discovery = [-1 for _ in range(n)]
    arival = [-1 for _ in range(n)]
    time = 0
    for u in range(n):
        if not visited[u]:
            time = DFS_visit(G, u, visited, parent, time, arival, discovery)
    return discovery

def DFS_visit(G, u, visited, parent, time, arival, discovery):
    visited[u] = True
    arival[u] = time
    # time += 1
    for v in G[u]:
        if v is not None and not visited[v]:
            parent[v] = u
            time = DFS_visit(G, v, visited, parent, time, arival, discovery)
    discovery[u] = time  # czas przetworzenia
    time += 1
    return time

if __name__ == '__main__':
    edges = [[1, 2], [None], [3, 4], [5], [5], [None], [7], [None]]
    G = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [ 9, 10], [8], [8]]
    print(DFS(G, len(G)))
