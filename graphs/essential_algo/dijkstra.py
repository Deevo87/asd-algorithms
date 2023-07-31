from queue import PriorityQueue
from math import inf


def minDistance(G, dist, sptSet):
    min = 1e7
    n = len(G)
    min_index = None
    for v in range(n):
        if dist[v] < min and sptSet[v] == False:
            print(min)
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(G, s):
    n = len(G)
    q = PriorityQueue()
    visited = [False for _ in range(n)]
    D = [inf for _ in range(n)]
    Parent = [i for i in range(n)]
    D[s] = 0
    q.put((D[s], s))
    while not q.empty():
        u = q.get()[1]
        if not visited[u]:
            for v in range(n):
                if G[u][v] > 0 and not visited[v] and D[v] > D[u] + G[u][v]:
                    D[v] = D[u] + G[u][v]
                    #print(D[v] ,D)
                    Parent[v] = u
                    q.put((D[v], v))
            visited[u] = True
    return Parent, D

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
    print(dijkstra(x, 0))