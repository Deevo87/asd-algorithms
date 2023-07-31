from queue import PriorityQueue
from math import inf


def dijkstra(G, v, s, D, T):
    n = len(G)
    distance = [[inf] * D for _ in range(n)]
    distance[v][0] = 0
    visited = [[False] * D for _ in range(n)]
    p = [[-1] * D for _ in range(n)]
    K = PriorityQueue()
    K.put((0, v, 0))  # krotka - (dotychczaswoy koszt, wierzchołek, ile l benzyny mam dojezdzajac do wierzchołka)

    while not K.empty():

        cost_sum, v, tank_before = K.get()
        # obecny koszt
        # wierzchołek obecny
        # l benzyny które mam dojeżdżając


        if not visited[v][tank_before]:
            visited[v][tank_before] = True
            fuel = 0

            while fuel + tank_before <= D:
                for u, dist_to_u in G[v]:
                    if dist_to_u <= fuel + tank_before and distance[u][fuel + tank_before - dist_to_u] > cost_sum + fuel * T[v]:
                        distance[u][fuel + tank_before - dist_to_u] = cost_sum + fuel * T[v]
                        p[u][fuel + tank_before - dist_to_u] = v
                        K.put((cost_sum + fuel * T[v], u, fuel + tank_before - dist_to_u))
                fuel += 1
    for fuel in enumerate(p):
        print(fuel)
    return distance


A = [
    [(1, 3), (4, 2), (3, 3)],  # 0
    [(0, 3), (3, 4), (2, 5)],  # 1
    [(1, 5), (3, 2), (7, 1)],  # 2
    [(0, 3), (1, 4), (2, 2), (6, 4)],  # 3
    [(0, 2), (5, 3)],  # 4
    [(4, 3), (6, 4), (8, 3)],  # 5
    [(5, 4), (3, 4), (8, 2), (7, 3)],  # 6
    [(2, 1), (6, 3), (8, 1)],  # 7
    [(5, 3), (6, 2), (7, 1)]

]
T = [1, 3, 2, 2, 2, 2, 4, 4, 3]
print(dijkstra(A, 0, 8, 5, T))
