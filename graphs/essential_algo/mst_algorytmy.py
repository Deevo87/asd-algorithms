from queue import PriorityQueue
from math import inf
import networkx as nx
from random import paretovariate, randint
import time

'''
def find_i(i, parent):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, rank, a, b):
    x = find_i(a, parent)
    y = find_i(b, parent)

    if rank[x] < rank[y]:
        parent[x] = y

    elif rank[y] < rank[x]:
        parent[y] = x

    else:
        parent[y] = x
        rank[x] += 1


def Kruskal_krawedzie(G, n):
    result = []
    G = sorted(G, key=lambda x: x[2])

    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]

    count, index = 0, 0
    
    while count < n - 1 and index < len(G):
        u, v, w = G[index]
        index += 1

        x = find_i(u, parent)
        y = find_i(v, parent)

        if x != y:
            count += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    min_c = 0
    for i in result:
        min_c += i[2]
        
    return min_c
'''

def find(a, parents):
    while parents[a] != a:
        a = parents[a]
    return a


def union(a, b, parents, rank):
    x = find(a, parents)
    y = find(b, parents)
    
    if rank[x] < rank[y]:
        parents[x] = y 
    elif rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y 
        rank[x] += 1
        


def kruskal_algo(G, n):
    rank = [0 for _ in range(n)]
    parents = [i for i in range(n)]
    result = []

    G = sorted(G, key= lambda x: x[2])
    
    count = 0
    index = 0
    
    while count < n - 1 and index < len(G):
        x, y, weight = G[index]
        index += 1
        
        a = find(x, parents)
        b = find(y, parents)
        
        if a != b:
            count += 1
            result.append((u, v, weight))
            union(x,y,parents,rank)
    
    print(result)


def kruskal_matrix(G, n):
    min_c = 0
    parent = [i for i in range(n)]
    count = 0

    while count < n - 1:
        min = inf
        for i in range(n):
            for j in range(n):
                if G[i][j] is not inf and G[i][j] < min and find(i, parent) != find(j, parent):
                    min = G[i][j]
                    a = i
                    b = j

        parent[find(a, parent)] = find(b, parent)
        count += 1
        min_c += min

    return min_c


def minkey(key, mst):
    n = len(mst)
    min_value = inf
    min_index = 0

    for i in range(n):
        if key[i] < min_value and mst[i] == False:
            min_value = key[i]
            min_index = i

    return min_index


def prim_matrix(G, n):

    key = [inf] * n
    parent = [None] * n
    mst = [False] * n

    key[0] = 0
    parent[0] = 0

    for _ in range(n):
        u = minkey(key, mst)
        mst[u] = True

        for i in range(n):
            if G[u][i] > 0 and mst[i] == False and key[i] > G[u][i]:
                key[i] = G[u][i]
                parent[i] = u

    print(parent)
    return sum(key)


def prims_deque(G, n):

    adj = [[] for _ in range(n)]

    for u, v, w in G:
        adj[u].append((v, w))
        adj[v].append((u, w))

    key = [inf] * n
    parent = [-1] * n
    mst = [False] * n

    src = 0
    key[src] = 0

    q = PriorityQueue()
    q.put((0, src))

    while not q.empty():
        w, u = q.get()
        if mst[u] == True:
            continue

        mst[u] = True

        for i in adj[u]:
            v, weight = i[0], i[1]
            if mst[v] == False and key[v] > weight:
                key[v] = weight
                q.put((key[v], v))
                parent[v] = u

    return sum(key)


n = int(input("Ile wierzchołków: "))
k = int(input("Ile krawędzi(>=n): "))

min_wal = int(input("min przedział randint: "))
max_wal = int(input("max przedział randint: "))
G = nx.gnm_random_graph(n, k)
print(G.edges())

g2 = []
g = [[inf for _ in range(n)] for _ in range(n)]

for (u, v) in G.edges:
    xd = randint(min_wal, max_wal)
    g[u][v] = xd
    g[v][u] = xd
    g2.append((u, v, xd))

print("Algorytm Kruskala - lista sąsiedztwa",)
s3 = time.time()
x = kruskal_algo(g2, n)
s4 = time.time()
print(f"Wynik: {x}, Czas = {(s4-s3)*1000:.2f}")

print("Algorytm Prima - macierz sąsiedztwa",)
s5 = time.time()
x = prim_matrix(g, n)
s6 = time.time()
print(f"Wynik: {x}, Czas = {(s6-s5)*1000:.2f}")

print("Algorytm Prima - lista sąsiedztwa",)
s7 = time.time()
x = prims_deque(g2, n)
s8 = time.time()
print(f"Wynik: {x}, Czas = {(s8-s7)*1000:.2f}")

print("Algorytm Kruskala - macierz sąsiedztwa",)
s1 = time.time()
x = kruskal_matrix(g, n)
s2 = time.time()
print(f"Wynik: {x}, Czas = {(s2-s1)*1000:.2f}")