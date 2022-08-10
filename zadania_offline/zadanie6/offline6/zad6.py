#Rafał Laskowski
from zad6testy import runtests
from collections import deque

'''złożoność czasowa algorytmu to O(V + E + q)
    Najpierw znajduję najkrótszą ścieżkę za pomocą algorytmu BFS zapisując odległości od wierchołka s w tablicy D.
    Następnie zaczynając od wierzchołka docelowego (t) patrze na wychodzące z niego krawędzie (które mają odległość 
    mniejszą o 1 od t) i szukam wierzchołka, w którym się zbiegnął, jeżeli taki nie istnieje to istnieje więcej niż 
    jedna najkrótsza ścieżka (wtedy zwracam None). Jeżeli już znajdę wierzchołek, w którym zbiegają się wszystkie 
    krawędzie (o najmniejszej odległości od s) wychodzące z t to patrzę na sąsiadów naszego docelowego wierzchołka i 
    jeżeli więcej niż jeden jego sąsiad ma odległość o jeden mniejszą do niego to powtarzam algorytm opisany wyżej, 
    jeżeli nie to zwracam odpowiedź. 
'''

def to_return(G, D, x):
    for u in G[x]:
        if D[u] == D[x] - 1:
            if u > x:
                return x, u
            return u, x
    return None


def longer(G, s, t):
    n = len(G)
    que = deque()
    V = [False for _ in range(n)]
    D = [-1 for _ in range(n)]
    V[s] = True
    D[s] = 0
    que.append(s)
    while que:
        w = que.popleft()
        for u in G[w]:
            if not V[u]:
                V[u] = True
                D[u] = D[w] + 1
                que.append(u)
    if D[t] == -1 or D[s] == -1:
        return None
    que2 = deque()
    que2.append(t)
    tmp = -1
    licz = 0
    if D[t] - 1 == D[s]:
        return s, t
    while que2:
        p = que2.popleft()
        for u in G[p]:
            if u == tmp:
                licz1 = 0
                x = tmp
                for v in G[x]:
                    if D[v] == D[x] - 1:
                        licz1 += 1
                        que2.append(x)
                if licz1 == 1:
                    return to_return(G, D, tmp)
            if D[p] - 1 == D[u]:
                tmp = u
                licz += 1
                que2.append(u)
        if licz == 1:
            licz1 = 0
            x = tmp
            for v in G[x]:
                if D[v] == D[x] - 1:
                    licz1 += 1
                    que2.append(x)
            if licz1 == 1:
                return to_return(G, D, tmp)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
