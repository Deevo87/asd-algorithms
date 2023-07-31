from collections import deque
from dis import dis
from queue import PriorityQueue
from math import inf
import networkx as nx
from random import randint
from random import randrange
import time

def BFS(G, n, s, t, p):
    visited = [False for _ in range(n)]

    q = deque()
    visited[s] = True
    q.append(s)

    while q:
        u = q.pop()
        for i in range(n):
            if visited[i] == False and G[u][i] > 0:
                visited[i] = True 
                p[i] = u
                q.append(i)
               
    return visited[t] == True

  
def Edmonds(G, n, s, t):
    
    for i in G:
        print(i)
    
    print(n)
    
    p = [-1 for _ in range(n)]
    flow = 0
    
    while BFS(G, n, s, t, p):
        p_flow, x = inf, t
        while x != s:
            u = p[x]
            p_flow = min(p_flow, G[u][x])
            x = p[x]

        flow += p_flow
        x = t
        while x != s:
            u = p[x]
            G[u][x] -= p_flow
            G[x][u] += p_flow
            x = p[x]
    
    return flow


n = int(input("Ile wierzchołków: "))
k = int(input("Ile krawędzi(>=n): "))

min_wal = int(input("min przedział randint: "))
max_wal = int(input("max przedział randint: "))
G = nx.gnm_random_graph(n, k)

g2 = []
g = [[inf for _ in range(n)] for _ in range(n)]

for (u, v) in G.edges:
    xd = randrange(min_wal, max_wal)
    g[u][v] = xd
    g[v][u] = xd
    g2.append((u, v, xd))

print(Edmonds(g, n, 0, n-1))