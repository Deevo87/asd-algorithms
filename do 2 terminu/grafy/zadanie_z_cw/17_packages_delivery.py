# Byteland is a land containing N cities and N-1 two-way roads. The road system creates a consistent
# graph. We are given a list of K cities to which we have to deliver packages and being able to start
# and finish the route in any city, find the minimum distance that we must travel to deliver all packages.

def packages_delivery(G, s):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    dist = [0]*n
    dfs(G, s, visited, parent, dist)
    maks = max_ver_finder(dist)
    visited = [False] * n
    dist = [0] * n
    parent[maks] = -1
    dfs(G, maks, visited, parent, dist)
    start = max_ver_finder(dist)
    i = start
    diameter = [start]
    while parent[i] != -1:
        diameter.append(parent[i])
        i = parent[i]
    cnt = 0
    print(diameter)
    for x in range(n):
        if x == start:
            continue
        if x in diameter:
            cnt += 1
        else:
            print(x)
            cnt += 2
    return cnt

def dfs(G, x, visited, parent, dist):
    visited[x] = True
    for i in G[x]:
        if not visited[i]:
            dist[i] = dist[x] + 1
            parent[i] = x
            dfs(G, i, visited, parent, dist)

def max_ver_finder(dist):
    n = len(dist)
    maks = 0
    ind = -1
    for i in range(len(dist)):
        if maks < dist[i]:
            ind = i
            maks = dist[i]
    return ind



if __name__ == '__main__':
    graph = [[1], [0, 2], [1, 3, 4], [2, 6], [2, 5], [4], [3, 7, 8], [6], [6, 9, 10, 11],
             [8], [8], [8, 12, 16], [11, 13, 14], [12, 15], [12], [13], [11, 17, 18], [16], [16]]
    print(packages_delivery(graph, 0))