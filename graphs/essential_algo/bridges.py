from math import inf

def bridges(G):
    n = len(G)
    discovery = [inf]*n
    parent = [-1]*n
    visited = [False]*n
    low_s = [inf]*n
    res = []
    time = 0
    for i in range(n):
        if not visited[i]:
            time = dfs_visit(G, i, visited, parent, discovery, time, low_s, res)
    return res

def dfs_visit(G, u, visited, parent, discovery, time, low_s, res):
    visited[u] = True
    discovery[u] = time
    low_s[u] = time
    time += 1
    for x in G[u]:
        if not visited[x]:
            parent[x] = u
            time = dfs_visit(G, x, visited, parent, discovery, time, low_s, res)
            low_s[u] = min(low_s[x], low_s[u])
            if low_s[x] > discovery[u]:
                res.append([u, x])
        elif x != parent[u]:
            low_s[u] = min(low_s[u], discovery[x])
    return time

if __name__ == '__main__':
    edges2 = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]
    somsiady = [[] for _ in range(len(edges2))]
    for i in range(len(edges2)):
        somsiady[edges2[i][0]].append(edges2[i][1])
    print(somsiady)
    print(bridges(somsiady))