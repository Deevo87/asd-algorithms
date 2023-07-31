# The diameter of tree is the distance between its vertices that distance from each other is
# the most. Find algorithm that, assuming a tree (not necessary a binary) presented as a list
# of edges will return its diameter.

def diameter(E):
    maks_ver = 0
    for i in range(len(E)):
        maks_ver = max(E[i][0], E[i][1], maks_ver)
    graph = [[] for _ in range(maks_ver+1)]
    for i in range(len(E)):
        graph[E[i][0]].append(E[i][1])
        graph[E[i][1]].append(E[i][0])
    print(graph)
    #graph = E
    maks = 0
    ind = -1
    visited = [False] * (maks_ver + 1)
    dist = [0]*(maks_ver+1)
    dfs(graph, 0, visited, dist)
    for i in range(maks_ver+1):
        if maks < dist[i]:
            maks = dist[i]
            ind = i
    visited = [False] * (maks_ver + 1)
    dist = [0] * (maks_ver + 1)
    dfs(graph, ind, visited, dist)
    return max(dist)


def dfs(G, v, visited, dist):
    visited[v] = True
    for x in G[v]:
        if not visited[x]:
            dist[x] = dist[v] + 1
            print(dist)
            dfs(G, x, visited, dist)


if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
             [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]
    edd = [[1], [0, 2, 3], [1], [1, 4], [3, 5, 8], [4, 6, 7], [5], [5], [4, 9], [8, 10], [9, 11], [10], [13], [12]]
    print(diameter(edges))
