from dis import dis
from queue import PriorityQueue
from math import inf
import networkx as nx
from random import randint
from random import randrange
import time


def Floyd(G, n):
    n = len(G)
    dist = G
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in dist:
        print(i)
    

n = int(input("Ile wierzchołków: "))
k = int(input("Ile krawędzi(>=n): "))

min_wal = int(input("min przedział randint: "))
max_wal = int(input("max przedział randint: "))
G = nx.gnm_random_graph(n, k)

g2 = []
g = [[inf for _ in range(n)] for _ in range(n)]

for (u, v) in G.edges:
    xd = randrange(min_wal, max_wal)
    if randint(0, 1) == 0:
        g[u][v] = xd
    else:
        g[v][u] = xd

    #g[v][u] = xd
    #g2.append((u, v, xd))

Floyd(g, n)