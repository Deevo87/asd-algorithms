# Dijkstra's algorithm for finding the shortest paths in weighted graph on adjacency list.
from queue import PriorityQueue
from math import inf


# 1st solution:


def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    n = len(graph)
    q = PriorityQueue()
    q.put((0, source))
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)] * len(graph)
    print(distance)
    visited = [False] * len(graph)
    distance[source] = 0
    while not q.empty():
        dist, u = q.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                q.put((dist + v[1], v[0]))
        visited[u] = True
    return parent, distance


# 2nd solution:


def dijkstra_algorithm_2(graph, source):
    queue = PriorityQueue()
    distance = [inf] * len(graph)
    counter = len(graph)
    queue.put((0, source))
    while not queue.empty() and counter > 0:
        dist, v = queue.get()
        if dist < distance[v]:
            counter -= 1
            distance[v] = dist
            for edge in graph[v]:
                u, length = edge
                queue.put((dist + length, u))
    return distance


graph =  [[(1, 9), (2, 2)],
          [(0, 9), (3, 2), (4, 6)],
          [(0, 2), (3, 7), (5, 1)],
          [(1, 2), (2, 7), (4, 2), (5, 3)],
          [(1, 6), (3, 2), (6, 1)],
          [(2, 1), (3, 3), (6, 8)],
          [(4, 1), (5, 8)]]

parent, distance = dijkstra_algorithm(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i])
    i -= 1
print("----------")
distance_2 = dijkstra_algorithm_2(graph, 0)
i = len(parent) - 1
while i != 0:
    print(i, distance_2[i])
    i -= 1