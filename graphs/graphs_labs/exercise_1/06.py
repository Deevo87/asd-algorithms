# Proszę zaimplementować algorytm BFS tak, żeby znajdował najkrótsze ścieżki w grafie i następnie,
# żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego do wskazanego wierzchołka.

from queue import Queue
from math import inf

def find_shortest_paths(G):
    n = len(G)
    queue = Queue()
    queue.put(0)
    D = [inf for _ in range(n)]
    D[0] = 0
    visited = [False for _ in range(n)]
    visited[0] = True
    while not queue.empty():
        u = queue.get()
        for v in G[u]:
            if not visited[v]:
                min_distance = inf
                for g in G[v]:
                    min_distance = min(min_distance, D[g])
                D[v] = min_distance + 1
                visited[v] = True
                queue.put(v)
    return D

if __name__ == '__main__':
    graph = [[1, 2], [0, 3, 4], [0], [1, 5], [1, 6], [3, 7, 8], [4, 11], [5], [5, 9], [8, 10, 11], [9], [6, 9]]
    print(find_shortest_paths(graph))