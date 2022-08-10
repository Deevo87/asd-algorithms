from queue import PriorityQueue
from math import inf

def dijkstra(G,v,s,D,T):
    n = len(G)
    distance = [[inf]*D for _ in range(n)]
    distance[v][0] = 0
    visited = [[False]*D for _ in range(n)]
    p = [[-1]*D for _ in range(n)]
    K = PriorityQueue()
    K.put((0, v, 0)) # krotka - (dotychczaswoy koszt, wierzchołek, ile l benzyny mam dojezdzajac do wierzchołka)
    
    while not K.empty():
        
        x,y,z = K.get()
        # obecny koszt
        # wierzchołek obecny
        # l benzyny które mam dojeżdżając
        
        if y == s:
            return x
        
        if not visited[y][z]:
            visited[y][z] = True
            i = 0
            
            while i+z <= D:
                for a, b in G[y]:
                    if b <= i+z and distance[a][i+z-b] > x + i*T[y]:
                        distance[a][i+z-b] = x + i*T[y]
                        p[a][i+z-b] = y
                        K.put((x + i*T[y],a,i+z-b))
                i += 1

    return distance


A = [
    [(1,3),(4,2),(3,3)],    # 0
    [(0,3),(3,4),(2,5)],    # 1
    [(1,5),(3,2),(7,1)],    # 2
    [(0,3),(1,4),(2,2),(6,4)],  # 3
    [(0,2),(5,3)],      # 4
    [(4,3),(6,4),(8,3)]   ,  # 5
    [(5,4),(3,4),(8,2),(7,3)],  # 6
    [(2,1),(6,3),(8,1)], # 7
    [(5,3),(6,2),(7,1)]

]
T = [1,3,2,2,2,2,4,4,3]
print(dijkstra(A,0,8,5,T))