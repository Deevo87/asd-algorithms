# Mamy dany graf G = (V, E) z wagami w: E → N-{0} (dodatnie liczby naturalne). Chcemy znalezc scieżkę
# z wierzchołka u do v tak, by iloczyn wag był minimalny.
from queue import PriorityQueue
from math import inf, log2

def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + log2(v[1]):
        distance[v[0]] = distance[u] + log2(v[1])
        parent[v[0]] = u
        return True
    return False

def minimum_product(graph, source, end):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, source))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    result = [end, parent[end]]
    index = parent[end]
    while index != source:
        result.append(parent[index])
        index = parent[index]
    result.reverse()
    return parent, result


if __name__ == '__main__':
    G = [[(1, 20), (2, 30)],
             [(0, 20), (3, 12), (4, 11)],
             [(0, 30), (3, 18), (5, 2700)],
             [(1, 12), (2, 18), (8, 22), ],
             [(1, 11), (6, 15)],
             [(2, 2700), (7, 19), (8, 3)],
             [(4, 15), (8, 8)],
             [(5, 19)],
             [(3, 22), (5, 3), (6, 8)]]

    u, v = 0, 7
    print(minimum_product(G, u, v))