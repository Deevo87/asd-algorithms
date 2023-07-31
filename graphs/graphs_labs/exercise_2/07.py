# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
# miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci
# (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na grupki tak, żeby
# każda grupka mogła przebyć trasę bez rozdzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
# dostali się z A do B.
from queue import PriorityQueue
from math import inf


def relax(u, v, graph, distance, parent):
    act_distance = min(distance[u], graph[u][v])
    if act_distance > distance[v]:
        distance[v] = act_distance
        parent[v] = u
        return True
    return False


def tour_guide(graph, city_a, city_b, capacity, max_weight):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((max_weight, city_a))
    parent = [None] * n
    distance = [0] * n
    visited = [False] * n
    distance[city_a] = inf
    while not queue.empty():
        dist, u = queue.get()
        for v in range(n):
            if not visited[v] and graph[u][v] != 0 and relax(u, v, graph, distance, parent):
                queue.put((-graph[u][v], v))
        visited[u] = True
    result = [city_b, parent[city_b]]
    index = parent[city_b]
    while index != city_a:
        result.append(parent[index])
        index = parent[index]
    result.reverse()
    print(result)
    return parent, distance


if __name__ == '__main__':
    E = [(0, 1, 8), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14),
         (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]
    max_ver = -inf
    max_weight = -inf
    for i in range(len(E)):
        max_ver = max(max_ver, E[i][1], E[i][0])
        max_weight = max(max_weight, E[i][2])
    G = [[0 for _ in range(max_ver + 1)] for _ in range(max_ver + 1)]
    for i in range(len(E)):
        G[E[i][0]][E[i][1]] = E[i][2]
        G[E[i][1]][E[i][0]] = E[i][2]
    for i in range(max_ver):
        print(G[i])
    print(max_weight + 1)
    print(tour_guide(G, 0, 7, 20, max_weight + 1))
