# Let's imagine an underground labyrinth composed of huge caves connected by narrow corridors. In one
# of caves, the dwarves have built their settlement and each of the other caves has a number of trolls.
# The dwarves want to plan their defense in case of being attacked by trolls. They intend to sneak in
# and plant an explosive load in one of the corridors, so that the trolls living beyond this corridor
# have no path to reach the dwarven settlement. Which of the corridors should be blown up to cut off
# trolls' access to the dwarven settlement.
from math import inf
from queue import Queue


def dwarves_and_trolls(G, T, s):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    arrival = [0]*n
    low = [inf]*n
    time = 0
    res = []
    T[s] = inf
    wages = [0]*n
    wages[s] = inf
    dfs_visit_special(G, s, visited, parent, low, arrival, time, wages, T)
    for i in range(n):
        if low[i] == arrival[i] and parent[i] != -1:
            res.append([parent[i], i])
    maks = 0
    corr = 0
    for x in res:
        tmp = bfs(G, x[0], x[1], T)
        if maks < tmp:
            maks = tmp
            corr = x
    return corr


def bfs(G, start, stop, T):
    n = len(G)
    visited = [False]*n
    visited[start] = visited[stop] = True
    q = Queue()
    q.put(start)
    cnt = T[start]
    while not q.empty():
        x = q.get()
        for i in G[x]:
            if not visited[i]:
                cnt += T[i]
                q.put(i)
                visited[x] = True
    return cnt


def dfs_visit_special(G, x, visited, parent, low, arrival, time, wages, T): # dfs "special" to dfs do algorytmów z mostów
    visited[x] = True
    arrival[x] = low[x] = time
    time += 1
    for v in G[x]:
        if not visited[v]:
            parent[v] = x
            time = dfs_visit_special(G, v, visited, parent, low, arrival, time, wages, T)
            low[x] = min(low[x], low[v])
        elif v != parent[x]:
            low[x] = min(low[x], arrival[v])
    # if parent[x] != -1: #najbardziej specialna część jest tutaj bo zapisuje sobie wagi :3
    #     wages[x] += T[x]
    #     wages[parent[x]] = max(wages[parent[x]], wages[x])
    #     #print(wages, x)
    return time



if __name__ == '__main__':
    graph = [[1, 2, 3, 4], [0, 2, 5, 6], [0, 1, 3], [0, 2], [0, 9, 10], [1, 7, 8],
             [1], [5, 8], [5, 7], [4, 10], [4, 9, 11], [10]]
    trolls = [1, 2, 8, 7, 17, 4, 13, 3, 12, 3, 1, 11]
    print(dwarves_and_trolls(graph, trolls, 0))
    graph2 = [[1, 2], [0, 3], [0, 3], [1, 2, 4, 8], [3, 5, 7], [4, 6], [5, 7], [4, 6], [3, 9, 10], [8, 10], [8, 9]]
    trolls2 = [1, 3, 3, 5, 10, 2, 3, 4, 1, 1, 1]
    print(dwarves_and_trolls(graph2, trolls2, 9))
