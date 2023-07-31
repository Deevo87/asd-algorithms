# We have a layout of dominoes. We have it as a list of pairs [a, b]. If we knock over block a, block
# b will also fall over. Find the minimum number of blocks that need to be knocked over by hand so that
# all dominoes are downed.

def domino(G, s):
    n = len(G)
    maks = 0
    for i in range(n):
        maks = max(G[i][0], G[i][1], maks)
    graph = [[]for _ in range(maks+1)]
    for i in range(n):
        graph[G[i][0]].append(G[i][1])
    scc_G = SSC(graph)
    i = 0
    while i < len(scc_G):
        if len(scc_G[i]) == 0:
            del scc_G[i]
        else:
            i += 1
    for i in range(len(G)):
        for j in range(len(scc_G)):
            if len(scc_G[j]) > 1:
                if G[i][0] in scc_G[j]:
                    G[i][0] = scc_G[j][0]
                if G[i][1] in scc_G[j]:
                    G[i][1] = scc_G[j][0]
    i = 0
    while i < len(G):
        if G[i][0] == G[i][1]:
            G.remove(G[i])
        else:
            i += 1
    for i in range(len(G)):
        for j in range(len(scc_G)):
            if G[i][0] in scc_G[j]:
                G[i][0] = j
                break
    for i in range(len(G)):
        for j in range(len(scc_G)):
            if G[i][1] in scc_G[j]:
                G[i][1] = j
    maks = 0
    for i in range(len(G)):
        maks = max(G[i][0], G[i][1], maks)
    degradated_G = [[] for _ in range(maks+1)]
    for i in range(len(G)):
        degradated_G[G[i][0]].append(G[i][1])
    print(degradated_G)
    visited = [False for _ in range(maks+1)]
    parent = [-1 for _ in range(maks+1)]
    for i in range(len(degradated_G)):
        if not visited[i]:
            dfs_visit2(degradated_G, i, visited, parent)
    cnt = 0
    for i in range(maks+1):
        if parent[i] == -1:
            cnt += 1
    return cnt


def dfs_visit2(G, x, visited, parent):
    visited[x] = True
    for i in G[x]:
        if not visited[i]:
            parent[i] = x
            dfs_visit2(G, i, visited, parent)

def dfsUTIL(G, x, visited, stack, parent):
    visited[x] = True
    for v in G[x]:
        if not visited[v]:
            parent[v] = x
            dfsUTIL(G, v, visited, stack, parent)
    stack.append(x)

def transpose_graph(G, new_G):
    n = len(G)
    for i in range(n):
        for j in G[i]:
            new_G[j].append(i)

def dfs_visit(G, s, visited, index, result):
    visited[s] = True
    result[index].append(s)
    for v in G[s]:
        if not visited[v]:
            dfs_visit(G, v, visited, index, result)

def SSC(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    stack = []
    for x in range(n):
        if not visited[x]:
            dfsUTIL(G, x, visited, stack, parent)
    new_G = [[] for _ in range(n)]
    transpose_graph(G, new_G)
    i = 0
    visited = [False for _ in range(n)]
    result = [[] for _ in range(n)]
    while len(stack):
        x = stack.pop()
        if not visited[x]:
            dfs_visit(new_G, x, visited, i, result)
            i += 1
    return result


if __name__ == '__main__':
    graphh = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 5], [4, 2], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]
    print(domino(graphh, 0))