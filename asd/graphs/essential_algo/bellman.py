from dis import dis
from queue import PriorityQueue
from math import inf
import networkx as nx
from random import randint
from random import randrange
import time

def BallmanFord(G, n, s):
    dist = [inf for _ in range(n)]
    dist[s] = 0
    
    
    for _ in range(n - 1):
        for u,v,w in G:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    for u,v,w in G:
        if dist[u] != inf and dist[u] + w < dist[v]:
            print("Negative cycle")
            return 
            
    print(dist)
    
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
    
for i in g:
    print(i)

BallmanFord(g2, n, 0)