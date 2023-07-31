from collections import deque
from dis import dis
from queue import PriorityQueue
from math import inf
import weakref
import networkx as nx
from random import randint
import time

def dijkstra(G, s, n):
    adj = [[] for _ in range(n)]
    
    for u, v, w in G:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    dist = [inf for _ in range(n)]
    dist[s] = 0
    
    q = PriorityQueue()
    q.put((0, s))
    
    while not q.empty():
        w1, u = q.get()
        
        for v, w2 in adj[u]:
            # relax
            if dist[v] > dist[u] + w2:
                dist[v] = dist[u] + w2
                q.put((dist[v], v))
                
    print(dist)
        

def find_min(dist,min_distance):
    min_value = inf
    
    for i in range(n):
        if dist[i] < min_value and min_distance[i] == False:
            min_value = dist[i]
            min_index = i
    
    return min_index


def dijkstra_macierz(G, s):
    n = len(G)
    dist = [inf for _ in range(n)]
    dist[s] = 0
    
    min_distance = [False for _ in range(n)]
    
    for _ in range(n):
        x = find_min(dist, min_distance)
        min_distance[x] = True
        
        for y in range(n):
            if G[x][y] > 0 and min_distance[y] == False and dist[y] > dist[x] + G[x][y]:
                dist[y] = dist[x] + G[x][y]
        
    print(dist)
    
    
def dijkstra_v2(G, s, n):
    dist = [inf for _ in range(n)]
    dist[s] = 0
    
    for u, v, w in G:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    q = PriorityQueue()
    q.put((0, s))
    
    while not q.empty():
        weight, u = q.get()
        
        for v, weight_2 in adj[u]:
            if dist[v] > dist[u] + weight_2:
                dist[v] = dist[u] + weight_2
                q.put((dist[v], v))
    
    print(dist)
    

n = int(input("Ile wierzchołków: "))
k = int(input("Ile krawędzi(>=n): "))

min_wal = int(input("min przedział randint: "))
max_wal = int(input("max przedział randint: "))
G = nx.gnm_random_graph(n, k)

g2 = []
g = [[inf for _ in range(n)] for _ in range(n)]
adj = [[]for _ in range(n)]


for (u, v) in G.edges:
    xd = randint(min_wal, max_wal)
    g[u][v] = xd
    g[v][u] = xd
    g2.append((u, v, xd))

print(dijkstra(g2, 0, n))
print(dijkstra_v2(g2, 0, n))
print(dijkstra_macierz(g, 0))
