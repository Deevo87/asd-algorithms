# Zadanie 2. (domkniecie przechodnie) Prosze zaimplementowac algorytm obliczajacy domkniecie przechodnie
# grafu reprezentowanego w postaci macierzowej (domkniecie przechodnie grafu G, to graf nad tym
# samym zbiorem wierzchołków, który dla kazdych dwóch wierzchołków u i v ma krawedz z u do v wtedy i
# tylko wtedy, gdy w G istnieje sciezka z u do v.

def closure(G):
    n = len(G)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                G[u][v] = G[u][v] or (G[u][k] and G[u][v])
    return G