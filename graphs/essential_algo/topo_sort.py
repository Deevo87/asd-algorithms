def top_sort(G, n): #na liście sąsiedztwa
    V = [False]*n
    P = [-1]*n
    T = [-1]*2*n
    time = -1
    for v in range(n):
        if not V[v]:
            time = DFS_visit(G, v, P, V, T, time)
    res = [-1]*n
    cnt = n-1
    for i in range(2*n):
        if T[i] != -1 and cnt >= 0:
            res[cnt] = T[i]
            cnt -= 1
    return res

def DFS_visit(G, u, P, V, T, time):
    V[u] = True
    time += 1
    for v in G[u]:
        if not V[v]:
            P[v] = u
            time = DFS_visit(G, v, P, V, T, time)
    T[time] = u
    time += 1
    return time

def topological_sort_dfs(G, v, visited, A):
    visited[v] = True
    for x in G[v]:
        if not visited[x]:
            topological_sort_dfs(G, x, visited, A)
    A.append(v)

def topological_sort(G):
    n = len(G)
    visited = [False]*n
    A = []
    for i in range(n):
        if not visited[i]:
            topological_sort_dfs(G, i, visited, A)
    A = A[::-1]
    return A

if __name__ == '__main__':
    edges = [[1, 2], [None], [3, 4], [5], [5], [None], [7], [None]]
    n = 8
    somsiady = [[]for _ in range(n)]
    edges2 = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
    for i in range(len(edges2)):
        somsiady[edges2[i][0]].append(edges2[i][1])
    print(somsiady)
    print(top_sort(somsiady, n))
    print(topological_sort(somsiady))