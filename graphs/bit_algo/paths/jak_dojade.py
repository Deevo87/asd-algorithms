# We are given two-dimensional array G which represents adjacency matrix of the weighted directed
# graph that corresponds to the road map (weights are the distances, the number -1 means that there
# is no edge). In some vertices there are petrol stations, we are given their list P. A full tank of
# fuel is enough to cover the distance d. When entering the station, the car is always fully refueled.
# Implement an algorithm which searches for the shortest possible route from vertex A to vertex B, if
# there is one and returns a list of consecutive visited vertices on the route (we assume that there
# is also a petrol station in vertex A, car can only travel distance d without refueling).

#SOLUTION
# 1) I made array to store which one are the stations and find it on O(1)
# 2) Secondly I created dxn arrays to store if the vertex was visited, what was the distance from it and to know who is
#   his parent. Basically I split vertexes depending on the amount of petrol with witch we are arriving. I don't track
#   it only on starting vertex and on the vertexes which are stations (its made for ease of finding path).
# 3) I perform simply dijkstra algorithm on the multivertex graph checking if I am able to reach the destination
#   and if I have enough petrol.
# 4) Using arrays of parents (stores information about the level of fuel which I came with to the vertex and vertex from
# which I came) I find the path.
# Time complexity: O(V^2)

from queue import PriorityQueue
from math import inf

def relax(graph, distance, u, v, tank, is_station, parent, d):
    curr_tank = tank - graph[u][v]
    if curr_tank < 0:
        return False
    if is_station[v]:
        curr_tank = d
    if distance[v][curr_tank] > distance[u][tank] + graph[u][v]:
        distance[v][curr_tank] = distance[u][tank] + graph[u][v]
        parent[v][curr_tank] = u, tank
        return True
    return False

def paths_with_refueling(graph, station, d, a, b):
    n = len(graph)
    is_station = [False for _ in range(n)]
    for s in station:
        is_station[s] = True

    visited = [[False for _ in range(d+1)] for _ in range(n)]
    distance = [[inf for _ in range(d+1)] for _ in range(n)]
    parent = [[(None, None) for _ in range(d+1)] for _ in range(n)]
    for i in range(d+1):
        distance[a][i] = 0
    q = PriorityQueue()
    q.put((0, a, d))

    while not q.empty():
        dist, u, tank = q.get()
        for v in range(n):
            if not visited[u][tank] and graph[u][v] != -1 and relax(graph, distance, u, v, tank, is_station, parent, d):
                curr_tank = tank
                if is_station[v]:
                    curr_tank = d
                else:
                    curr_tank -= graph[u][v]
                q.put((dist + graph[u][v], v, curr_tank))
        visited[u][tank] = True

    if distance[a][b] == inf:
        return None

    min_dist = inf
    fuel = inf
    for i in range(n):
        if min_dist > distance[b][i]:
            min_dist = distance[b][i]
            fuel = i
    path = []
    start = [b, fuel]
    while start[0] is not None:
        path.append(start[0])
        start = parent[start[0]][start[1]]
    path.reverse()
    return path


if __name__ == '__main__':
    G = [[-1, 6, -1, 5, 2],
             [-1, -1, 1, 2, -1],
             [-1, -1, -1, -1, -1],
             [-1, -1, 4, -1, -1],
             [-1, -1, 8, -1, -1]]
    P = [0, 1, 3]
    print(paths_with_refueling(G, P, 5, 0, 2))