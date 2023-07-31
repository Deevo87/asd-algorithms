# We get as input a directed acyclic graph (DAG - Directed Acyclic Graph) as a list of edges and pair
# of vertices s and t. Find how many possible paths is between s and t.

def paths_in_DAG(E, s, f):
    n = len(E)
    maks = 0
    for i in range(n):
        maks = max(maks, E[i][0], E[i][1])
    print(maks)
    graph = [[] for _ in range(maks+1)]
    for i in range(n):
        graph[E[i][0]].append(E[i][1])
    print(E)
    print(graph)
    visited = [False for _ in range(maks+1)]
    parent = [-1 for _ in range(maks+1)]
    cnt = 0
    cnt = dfs_visit(graph, s, visited, parent, cnt, f)
    print(parent)
    print(visited)
    return cnt


def dfs_visit(G, x, visited, parent, cnt, goal):
    if x == goal:
        cnt += 1
        return cnt
    visited[x] = True
    for v in G[x]:
        if not visited[v]:
            parent[v] = x
            cnt = dfs_visit(G, v, visited, parent, cnt, goal)
    visited[x] = False
    return cnt


#########################################
###### 2 rozwiązanie aka dynamik ########
#########################################

# def dfs(graph, source, visited, DP):
#     visited[source] = True
#     for v in graph[source]:
#         if not visited[v]:
#             DP[v] = 1
#             dfs(graph, v, visited, DP)
#         elif visited[v]:
#             DP[v] += 1
#             dfs(graph, v, visited, DP)
#
#
# def paths_in_DAG(edges, start, end):
#     max_vertex = 0
#     for i in range(len(edges)):
#         max_vertex = max(max_vertex, max(edges[i]))
#     graph = [[] for _ in range(max_vertex + 1)]
#     for i in range(len(edges)):
#         graph[edges[i][0]].append(edges[i][1])
#     DP = [0] * len(graph)
#     visited = [False] * len(graph)
#     dfs(graph, start, visited, DP)
#     print(DP)
#     return DP[end]





if __name__ == '__main__':
    edges = [[0, 1], [1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [6, 4], [5, 6], [5, 4]]
    start = 1
    end = 4
    print(paths_in_DAG(edges, start, end))