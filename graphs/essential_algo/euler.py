
from collections import deque


def Euler(G):
    G_copy = [i[:] for i in G]
    
    n = len(G)
    #parent = [None for _ in range(n)]
    #times = [-1 for _ in range(n)]
    #times[0] = 0
    result  = deque()
    
    for i in range(n):
        if G_copy[0][i] !=0: 
            G_copy[0][i], G_copy[i][0] = 0, 0
            DFSvisit(G_copy, i, result)
    
    print(result)


def DFSvisit(G, u, result):   
     
    for i in range(len(G)):
        if G[u][i] != 0:
            G[u][i], G[i][u] = 0, 0
            #parent[i] = u
            #times[i] = times[u] + 1
            DFSvisit(G, i, result)
    
    result.appendleft(u)
    


G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0, 1],
     [0, 1, 1, 0, 1, 1],
     [0, 0, 0, 1, 0, 1],
     [0, 1, 1, 1, 1, 0],]

Euler(G)