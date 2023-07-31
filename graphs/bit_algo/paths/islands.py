# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The cost of the overflight from
# island to island costs 8B, ferry crossing costs 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the cost of the trip. We are given an array G that specifies
# the cost of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels cost from island A
# to island B. If such a route doesn't exist, the function should return None.

# SOLUTION
# performing dijkstra on graph and check if we are not using the transport used before
# it could be done on matrix but i did it on adj list
# and it there is no need to diverse adj array on 3 columns (for bridge, ferry and flight)
# time complexity is O(V^2)

from queue import PriorityQueue
from math import inf


def relax(distance, u, v, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def islands(graph, s, end):
    n = len(graph)
    graph = turn_into_adj_list(graph)
    for i, element in enumerate(graph):
        print(i, element)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    distance[s] = 0
    q = PriorityQueue()
    for i in range(3):
        q.put((0, s, i))
    while not q.empty():
        dist, u, transport = q.get()
        # print(u, dist)
        for t in range(3):
            if t != transport:
                for v in graph[u][t]:
                    if not visited[v[0]] and relax(distance, u, v, parent):
                        q.put((dist + v[1], v[0], t))
                visited[u] = True
    print(distance)
    path = []
    result = distance[end]
    while end != -1:
        path.append(end)
        end = parent[end]
    path.reverse()
    print(path)
    return result


def turn_into_adj_list(graph): #0 - bridge, 1 - ferry, 2 - flight
    n = len(graph)
    adj = [[[] for _ in range(3)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                adj[j][0].append((i, 1))
            elif graph[i][j] == 5:
                adj[j][1].append((i, 5))
            elif graph[i][j] == 8:
                adj[j][2].append((i, 8))
    return adj

if __name__ == '__main__':
    G = [[0, 5, 1, 8, 0, 0, 0],
         [5, 0, 0, 1, 0, 8, 0],
         [1, 0, 0, 8, 0, 0, 8],
         [8, 1, 8, 0, 5, 0, 1],
         [0, 0, 0, 5, 0, 1, 0],
         [0, 8, 0, 0, 1, 0, 5],
         [0, 0, 8, 1, 0, 5, 0]]
    print(islands(G, 5, 2))
