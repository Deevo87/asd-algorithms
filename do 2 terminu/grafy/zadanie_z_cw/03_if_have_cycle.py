def detect_cycle(G, s):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    # for i in range(n):
    #     if not visited[i]:
    return dfs_visit(G, s, visited, parent)

def dfs_visit(G, x, visited, parent):
    visited[x] = True
    for v in G[x]:
        if not visited[v]:
            parent[v] = x
            if dfs_visit(G, v, visited, parent):
                return True
        elif visited[v] and parent[x] != v:
            return True
    return False



if __name__ == '__main__':
    # graph has a cycle
    graph1 = [[1, 2, 3], [0, 7], [0, 5], [0, 5], [0, 6, 7], [2, 3, 6], [4, 5], [1, 4]]
    print(detect_cycle(graph1, 0))

    # graph doesn't have a cycle
    graph2 = [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]
    print(detect_cycle(graph2, 0))

    graph3 = [[1, 5], [0, 2], [1, 3, 4], [2], [2, 5], [0, 4, 6], [5]]
    print(detect_cycle(graph3, 0))