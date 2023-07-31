# We are given a weighted graph G with positive weights. There is also given a list of edges E' that
# do not belong to the graph, but they are edges between the vertices in G. The two vertices s and t
# are also given. Determine which edge from E' should be added to the graph G to reduce the distance
# between s and t as much as possible. If neither edge lower the distance between s and t, the
# algorithm should return False.

# SOLUTION
# 1) use djikstra algorithm to check distances from s to any other vertex
# 2) secondly create a loop through table of edges and perform:
#       distance[t] - distance[u] + weight + (distance[t] - distance[v])
#       where distance[t] - distance[v] is distance from t to v
#       and distance[u] + weight is the distance from s to v
# if above calculations are more than 0 and more than current best weight we save it as a result
# complexity O(V^2) + O(E)

from queue import PriorityQueue
from math import inf


def relax(graph, distance, parent, u, v):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u
        return True
    return False


def djikstra_matrix(graph, s):
    n = len(graph)

    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    distance[s] = 0

    while not q.empty():
        dist, u = q.get()
        for v in range(n):
            if not visited[v] and graph[u][v] != 0 and relax(graph, distance, parent, u, v):
                q.put((dist + graph[u][v], v))
        visited[u] = True
    return distance, parent


def edge_reducing_the_distance(graph, edges, s, t):
    distance, parent = djikstra_matrix(graph, s)
    print(distance)

    best_path = -inf
    golden_u = inf
    golden_v = inf
    for u, v, weight in edges:
        new_path_weight = distance[t] - distance[u] + weight + (distance[t] - distance[v])
        print(u, v, new_path_weight)
        if 0 <  new_path_weight and best_path < new_path_weight:
            golden_u, golden_v = u, v
            best_path = new_path_weight
    if golden_u == inf:
        return False
    return golden_u, golden_v, best_path


if __name__ == '__main__':
    G = [[0, 0, 1, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0],
         [1, 0, 0, 6, 4, 8, 0, 0],
         [2, 0, 6, 0, 0, 0, 0, 0],
         [0, 5, 4, 0, 0, 0, 0, 6],
         [0, 0, 8, 0, 0, 0, 4, 1],
         [0, 0, 0, 0, 0, 4, 0, 7],
         [0, 0, 0, 0, 6, 1, 7, 0]]
    E = [(0, 1, 3), (3, 5, 5), (3, 6, 6), (4, 5, 3)]
    print(edge_reducing_the_distance(G, E, 0, len(G) - 1))
