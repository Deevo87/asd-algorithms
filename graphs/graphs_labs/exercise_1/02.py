# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza czy
# w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest
# przez macierz sasiedztwa A.

def four_length_cycle(G):
    n = len(G)
    for i in range(n):
        for j in range(i+1, n):
            cnt = 0
            result = [i, j]
            for x in range(n):
                if x != i and G[i][x] == G[j][x] == 1:
                    cnt += 1
                    result.append(x)
                if cnt == 2:
                    print(result)
                    return True
    return None


if __name__ == '__main__':
    graph = [[0, 0, 1, 0, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [1, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 1, 0]]
    result = four_length_cycle(graph)
    print(result)