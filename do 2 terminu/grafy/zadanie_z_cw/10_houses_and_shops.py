# We have a map of city where are houses and shops. There are also roads (each of length 1)
# that connect a house with a house or a house with a shop. We have to find for each home
# the distance to the nearest shop.
from queue import Queue
from math import inf

from queue import Queue

#lepszy bfs po sklepach
# def BFS(G, Q, V):
#     while not Q.empty():
#         v = Q.get()
#         for u in G[v]:
#             if V[u] == -1:
#                 V[u] = V[v] + 1
#                 Q.put(u)
#
#
# def houses_and_shops(R, S):
#     max_vertex = -1
#     for i in range(len(R)):
#         max_vertex = max(max_vertex, max(R[i]))
#     n = max_vertex + 1
#     graph = [[] for _ in range(n)]
#     for i in range(len(R)):
#         graph[R[i][0]].append(R[i][1])
#         graph[R[i][1]].append(R[i][0])
#     V = [-1 for i in range(n)]
#     Q = Queue()
#     for i in S:
#         Q.put(i)
#         V[i] = 0
#     BFS(graph, Q, V)
#     return V


#bfs po sklepach ;3
def bfs(G, S):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    D = [inf]*n
    q = Queue()
    q.put(S[0])
    visited[S[0]] = True
    D[S[0]] = 0
    while not q.empty():
        x = q.get()
        flag = False
        if x in S:
            flag = True
            D[x] = 0
        for v in G[x]:
            if not visited[v]:
                if flag: # ten pomysł z flagą to podjebałem, wcześniej tu miałem if x in S
                    D[v] = 1 # sprawdzam czy parent jest sklepem
                elif v in S: # sprawdzam czy obecny wierzchołek jest sklepem
                    D[v] = 0
                visited[v] = True
                parent[v] = x
                q.put(v)
            D[v] = min(D[v], D[x] + 1)
    return D


def houses_and_shops(R, S):
    max_vertex = -1
    for i in range(len(R)):
        max_vertex = max(max_vertex, max(R[i]))
    graph = [[] for _ in range(max_vertex + 1)]
    for i in range(len(R)):
        graph[R[i][0]].append(R[i][1])
        graph[R[i][1]].append(R[i][0])
    return bfs(graph, S)




if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
             [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
    shops = [2, 3, 9]
    print(houses_and_shops(edges, shops))