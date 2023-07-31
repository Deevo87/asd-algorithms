# Given a list of edges of the tree (not necessary binary) and highlighted vertex - the root.
# Each vertex creates its own sub-tree. For each vertex, find the number of vertices in its subtree.

def subtree_size(edges, ver):
    n = len(edges)
    maks = 0
    for i in range(n):
        maks = max(maks, max(edges[i][0], edges[i][1]))
    graph = [[] for _ in range(maks+1)]
    for i in range(n):
        graph[edges[i][0]].append(edges[i][1])
    print(graph)
    parent = [-1]*(maks+1)
    visited = [False]*(maks+1)
    vertex_cnt = [1]*(maks+1)
    dfs_visit(graph, ver, visited, parent, vertex_cnt)
    return vertex_cnt

def dfs_visit(G, x, visited, parent, vertex_cnt):
    visited[x] = True
    for i in G[x]:
        if not visited[i]:
            parent[i] = x
            dfs_visit(G, i, visited, parent, vertex_cnt)
    if parent[x] != -1:
        vertex_cnt[parent[x]] += vertex_cnt[x]
        #print(parent[x],vertex_cnt[parent[x]])


if __name__ == '__main__':
    EDS = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
             [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]
    print(subtree_size(EDS, 0))