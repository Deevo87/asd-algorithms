# In addition to length of edges, the graph has vertex costs associated with it. Let us define the
# cost of the path as the sum of the costs of its edges and sum of the costs of the vertices (along
# with the ends). Find the cheapest paths between the starting vertex and all the other vertices.
# Find a solution for directed and undirected graph.

# SOLUTION
# For undirected graph we add 1/2 of the cost of vertex to every edge which go from vertex and perform djikstra
#
# For directed graph we add the cost of vertex to directed edge and again perform djikstra
# complexity O(V^2) for both solutions
#
# here is solution only for undirected graph

from queue import PriorityQueue
from math import inf

def relax_undirected(u, v, distance):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        return True
    return False

def shortest_path_undirected(graph, vertices, source, finish):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j][1] += vertices[i] / 2 + vertices[graph[i][j][0]] / 2
    queue = PriorityQueue()
    queue.put((vertices[source] / 2, source))
    visited = [False] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = vertices[source] / 2
    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax_undirected(u, v, distance):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    distance[finish] += vertices[finish] / 2
    return distance[finish]


if __name__ == '__main__':
    undirected_graph = [[[1, 4], [2, 3]],
                        [[0, 4], [3, 6]],
                        [[0, 3], [3, 1], [4, 4], [6, 20]],
                        [[1, 6], [2, 1], [5, 3]],
                        [[2, 4], [6, 5]],
                        [[3, 3], [6, 5]],
                        [[2, 20], [4, 5], [5, 5]]]
    undirected_graph_vertices = [5, 4, 1, 2, 5, 4, 3]
    print(shortest_path_undirected(undirected_graph, undirected_graph_vertices, 0, 6))
