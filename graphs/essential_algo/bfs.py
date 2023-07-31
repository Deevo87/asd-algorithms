from queue import Queue

def BFS(G, s): #bfs bez żadnych komplikacji, nie działa na dla nie spójnych
    Q = Queue() # żeby odwiedził wszystkie trzeba go puszczać do czasu aż każy nie będzie visited (dla nie spójnych)
    n = len(G)
    visited = [False]*n
    D = [-1]*n
    P = [-1]*n
    visited[s] = True
    D[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v is not None and not visited[v]:
                P[v] = u
                D[v] = D[u]+1
                visited[v] = True
                Q.put(v)
    return P

if __name__ == '__main__':
    edges = [[1, 2], [None], [3, 4], [5], [5], [None], [7], [None]]
    G = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [2, 9, 10], [8], [8]]
    print(BFS(G, 0))
