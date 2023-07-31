# Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w Polsce. Jednym z głównych
# elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które tworza spójny graf
# połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi dodatkowo
# zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu działajacych stacji
# mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm podający
# kolejność wyłączania stacji.
# To samo zadanie, tylko inna treść:
# Dany jest spójny graf nieskierowany G = (V,E). Proszę zaproponować algorytm, który znajdzie taką
# kolejność usuwania wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie przestaje
# być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie dotykające go krawędzie).
from queue import Queue


def delete_vertices(G, s):
    Q = Queue()  # żeby odwiedził wszystkie trzeba go puszczać do czasu aż każy nie będzie visited (dla nie spójnych)
    n = len(G)
    visited = [False] * n
    D = [-1] * n
    P = [-1] * n
    visited[s] = True
    D[s] = 0
    Q.put(s)
    arrival = [s]
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if v is not None and not visited[v]:
                P[v] = u
                D[v] = D[u] + 1
                visited[v] = True
                arrival.append(v)
                Q.put(v)
    arrival.reverse()
    return arrival

if __name__ == '__main__':
    G = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [2, 9, 10], [8], [8]]
    print(delete_vertices(G, 0))