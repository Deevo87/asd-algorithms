# We are given a weighted graph G. Super cool path is one that is not only the shortest weighted path
# between v and u, but also has the fewest edges (in other words we are looking for the shortest paths
# in terms of the number of edges among the shortest paths in the weight sense). Find algorithm that
# for a given starting vertex s will find super cool paths to other vertices.

# SOLUTION
# Simple dijkstra with small change in relaxation, which consist only checking if number of edges is smaller
# than the actual when distances from parent are the same.
# Time complexity: O(ElogV)


from queue import PriorityQueue
from math import inf

def relax(distance, u, v, count, parent, ver_len):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        ver_len[v[0]] = count + 1
        return True
    elif distance[v[0]] == distance[u] + v[1] and count + 1 < ver_len[v[0]]:
        parent[v[0]] = u
        ver_len[v[0]] = count + 1
        return True
    return False

def super_cool_paths(graph, s):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    ver_len = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    q = PriorityQueue()
    distance[s] = 0
    ver_len[s] = 0
    q.put((0, 0, s))

    while not q.empty():
        dist, count, u = q.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(distance, u, v, count, parent, ver_len):
                q.put((dist + v[1], ver_len[v[0]], v[0]))
        visited[u] = True

    return distance, parent, ver_len

if __name__ == '__main__':
    G = [[(1, 1), (5, 1), (7, 2)],
             [(0, 1), (2, 1)],
             [(1, 1), (3, 1)],
             [(2, 1), (4, 1)],
             [(3, 1), (6, 1), (7, 2)],
             [(0, 1), (6, 2)],
             [(5, 2), (4, 1)],
             [(0, 2), (4, 2)]]

    d, p, vertices_length = super_cool_paths(G, 0)
    i = len(p) - 1
    while p[i] != -1:
        print(i, p[i], vertices_length[i])
        i -= 1