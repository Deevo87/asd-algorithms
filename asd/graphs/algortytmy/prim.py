from queue import PriorityQueue
from math import inf

def prim(G, s): # tablica sąsiedztwa
    n = len(G)
    q = PriorityQueue()
    P = [-1]*n
    visited = [False]*n
    W = [float(inf)]*n
    W[s] = 0
    q.put((W[s], s))
    while not q.empty():
        w, x = q.get()
        for v in G[x]:
            if not visited[v[1]] and W[v[1]] > v[0]:
                W[v[1]] = v[0]
                P[v[1]] = x
                q.put(v)
        visited[x] = True
    return P

if __name__ == '__main__':
    tab = [[(4, 1), (8, 7)], [(4, 0), (8, 2), (11, 7)], [(8, 1), (7, 3), (4, 5), (2, 8)],
           [(7, 2), (9, 4), (14, 5)], [(9, 3), (10, 5)], [(10, 4), (14, 3), (4, 2), (2, 6)],
           [(2, 5), (1, 7), (6, 8)], [(1, 6), (7, 8), (11, 1), (8, 0)], [(2, 2), (6, 6), (7, 7)]]
    print(prim(tab, 0))