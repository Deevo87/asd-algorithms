# Let G = (V, E) be a directed graph. We say that u,v belong to the same strongly connected
# component if there are directed paths from u to v and from v to u.


def SCC(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    new_graph = [[] for _ in range(len(graph))]
    print(graph)
    transpose_graph(graph, new_graph)
    print(new_graph)
    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    print(stack)
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1
    return result


def dfs(graph, source, visited, result, index):
    visited[source] = True
    result[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
    stack.append(source)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)


#graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
graph = [[1], [2], [3], [1, 5], [2], [6], [7], [8], [9], [6]]
print(SCC(graph))

#chujoza garbata
# def dfs(G, s, T, S, cnt):
#     n = len(G)
#     visited = [False]*n
#     P = [-1]*n
#     departue = [[i, -1] for i in range(n)]
#     time = 0
#     if s == 0:
#         for x in range(n):
#             if not visited[x]:
#                 time = dfs_visit(G, x, visited, departue, P, time, S, cnt)
#     else:
#         for x in T:
#             if not visited[x[0]]:
#                 S.append([])
#                 cnt += 1
#                 time = dfs_visit(G, x[0], visited, departue, P, time, S, cnt)
#         return S
#     return departue
#
# def dfs_visit(G, x, visited, departue, P, time, S, cnt):
#     visited[x] = True
#     S[cnt].append(x)
#     for v in G[x]:
#         if not visited[v]:
#             P[v] = x
#             time = dfs_visit(G, v, visited, departue, P, time, S, cnt)
#     time += 1
#     departue[x][1] = time
#     return time
#
# def reverse_edges(G):
#     n = len(G)
#     R = [[] for _ in range(n)]
#     for i in range(n):
#         for j in G[i]:
#             R[j].append(i)
#     return R
#
# def main(G):
#     T = []
#     S = [[]]
#     cnt = 0
#
#     T = dfs(G, 0, T, S, cnt)
#
#     G = reverse_edges(G)
#     T.sort(key=lambda x: x[1])
#     T = T[::-1]
#
#     S = []
#     cnt = -1
#     T = dfs(G, 1, T, S, cnt)
#     return T
#
# if __name__ == '__main__':
#     tab = [[1, 4], [2], [0, 10], [4, 6], [5], [3], [5], [8], [3, 9], [10], [7]]
#     #print(dfs(tab, 0))
#     edges2 = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
#     somsiady = [[] for _ in range(len(edges2))]
#     for i in range(len(edges2)):
#         somsiady[edges2[i][0]].append(edges2[i][1])
#     #print(somsiady)
#     graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
#     print(main(graph))