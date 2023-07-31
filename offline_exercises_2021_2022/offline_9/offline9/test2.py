# Python program for implementation
# of Ford Fulkerson algorithm
from collections import defaultdict

from math import inf
# This class represents a directed graph
# using adjacency matrix representation
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)

    # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    # Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0  # There is no flow initially
        while self.BFS(source, sink, parent):
            print(parent, 'PPPP')
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            for i in range(self.ROW):
                print(self.graph[i])
        return max_flow


# Create a graph given in the above diagram


C = [[0, 0, 0, 0, 0],
[10, 0, 0, 0, 0],
[0, 2, 0, 0, 0],
[0, 5, 0, 0, 0],
[0, 3, 0, 0, 0]]

C1 = [[0, 0, 9, 0, 0, 0, 0],#0
[7, 0, 0, 0, 0, 0, 0],#1
[0, 0, 0, 0, 0, 0, 0],#2
[3, 4, 7, 0, 0, 3, 0],#3
[0, 6, 0, 9, 0, 0, 8],#4
[0, 0, 9, 0, 0, 0, 0],#5
[0, 0, 0, 2, 0, 4, 0]]#6

C3 = [[0, 15, 7, 0, 6],
[0, 0, 2, 15, 3],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

C4 = [[0, 7, 0, 3, 0, 0, 0],
[0, 0, 0, 4, 6, 0, 0],
[9, 0, 0, 7, 0, 9, 0],
[0, 0, 0, 0, 9, 0, 2],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 3, 0, 0, 4],
[0, 0, 0, 0, 8, 0, 0]]
g = Graph(C4)

source = 2
sink = 4

print("The maximum possible flow is %d " % g.FordFulkerson(source, sink))

# This code is contributed by Neelam Yadav
