def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(x, y, parent, rank):
    x = find(parent, x)
    y = find(parent, y)
    if x == y: return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def MST(G, s):
    n = len(G)
    res = []
    vertexs = max(G, key=lambda tmp: tmp[1])[1]
    i = 0
    e = 0
    graph = [x[:] for x in G]
    graph.sort(key=lambda tmp: tmp[2])
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    while e < vertexs:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            res.append((u, v, w))
            union(x, y, parent, rank)
    return res


if __name__ == '__main__':
    Graph = [(0, 1, 16), (0, 2, 15), (0, 3, 37), (1, 2, 8), (1, 3, 22), (2, 3, 23)]
    print(MST(Graph, 0))