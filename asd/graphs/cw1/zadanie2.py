# Zadanie 2. (dobry poczatek) Wierzchołek v w grafie skierowanym nazywamy dobrym poczatkiem jesli
# kazdy inny wierzchołek mozna osiagnac sciezka skierowana wychodzaca z v. Prosze podac algorytm, który
# stwierdza czy dany graf zawiera dobry poczatek.

#1. dfs z czasami przetowrzenia
#2. dla największego odpalam jeszcze raz dfs
#3. patrzę czy każdy był visited

def dfs(G, s):
    def dfs_visit(G, u, visited, P, T):
        nonlocal time
        n = len(G)
        visited[u] = True
        for v in G[u]:
            if v is not None and not visited[v]:
                P[v] = u
                T = dfs_visit(G, v, visited, P, T)
        time += 1
        T[u] = time
        return T  # 0 to tablica przetworzenia, 1 to visited
    n = len(G)
    visited = [False for _ in range(n)]
    P = [-1 for _ in range(n)]
    T = [-1 for _ in range(n)]
    to_return = 0
    time = 0
    if s == -1:
        for u in range(n):
            if not visited[u]:
                to_return = dfs_visit(G, u, visited, P, T) #tablica przetworzenia
    else:
        tmp = dfs_visit(G, s, visited, P, T)
        to_return = visited
    return to_return


def good_start(G):
    check = dfs(G, -1) #tablica z czasami przetworzenia
    print(check)
    maks = -1
    vertex = -1
    for i in range(len(check)):
        if maks < check[i]:
            maks, vertex = check[i], i
    print(maks, vertex)
    check = dfs(G, vertex) #tablica visited
    for i in range(len(check)):
        if not check[i]:
            return False # False - jest wierzchołek nieodwiedzony
    return True # True - brak wierzchołków nieodwiedzonych


# działa w pyte
if __name__ == '__main__':
            #0       #1      #2    #3     #4   #5      #6    #7      #8
    graph = [[None], [0, 2, 3, 8], [6], [5, 6], [1], [None], [7], [None], [None]]
    print(dfs(graph, -1))
    print(good_start(graph))