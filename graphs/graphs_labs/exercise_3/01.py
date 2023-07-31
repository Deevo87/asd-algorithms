# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , |E|} (wagi krawędzi są
# parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o
# najmniejszej sumie wag, która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki
# nie ma to zwracamy inf).
from queue import PriorityQueue
from math import inf

def find_path(graph, s, t):
    graph.sort(key=lambda x: x[2]) # its only for optimalization of fidning path
    print(graph)
    n = len(graph)
    q = PriorityQueue()
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    distance[s] = 0
    q.put((0, inf, s))
    smallest_path = inf
    while not q.empty():
        dist, weight, u = q.get()
        print(dist, weight, u)
        if u == t:
            smallest_path = min(smallest_path, dist)
        for v in range(n):
            if not visited[v] and u == graph[v][0] and weight > graph[v][2]:
                q.put((dist + graph[v][2], graph[v][2], graph[v][1]))
                visited[v] = True
    return smallest_path


if __name__ == '__main__':
    G = [(0, 1, 15), (0, 2, 2), (0, 3, 6), (1, 2, 14), (1, 4, 7), (2, 5, 3), (2, 6, 4), (3, 7, 2),
             (4, 8, 6), (5, 9, 2), (6, 8, 5), (7, 9, 8), (8, 10, 5), (9, 10, 11)]
    print(find_path(G, 0, 10))