# Proszę zaproponować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci
# macierzowej (domknięcie przechodnie grafu G to taki graf H, że w H mamy krawędź z u do v wtedy
# i tylko wtedy gdy w G jest ścieżka skierowana z u do v).
from math import inf

def transitive_closure(graph):
    n = len(graph)
    distance = [[0] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 1
            elif graph[i][j] != 0:
                distance[i][j] = 1
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][v] == 1 or (graph[u][k] == 1 and graph[k][v] == 1):
                    distance[u][v] = 1
    return distance

if __name__ == '__main__':
    G = [    [0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0],
             [0, 0, 1, 0, 1],
             [0, 0, 1, 0, 0]]
    reach = transitive_closure(G)
    for i in range(len(reach)):
        print(reach[i])