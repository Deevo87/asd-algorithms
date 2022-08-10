from zad7ktesty import runtests


def poj_drzewa(T, V, x, g=0):  # x kordynaty, g glebokosc
    V[g][x] = True
    if T[g][x] == 0:
        return 0
    ng = len(T)
    n = len(T[0])
    s = T[g][x]
    if g < ng - 1 and not V[g + 1][x]:
        s += poj_drzewa(T, V, x, g + 1)
    if x < n - 1 and not V[g][x + 1]:
        s += poj_drzewa(T, V, x + 1, g)
    if x > 0 and not V[g][x - 1]:
        s += poj_drzewa(T, V, x - 1, g)
    if g > 0 and not V[g - 1][x]:
        s += poj_drzewa(T, V, x, g - 1)
    return s


def max_zysk(F, Z, P, l, i):
    if i < 0:
        return 0
    if l < 0:
        return 0
    if F[l][i] != 0:
        return F[l][i]
    mx = max_zysk(F, Z, P, l, i - 1)
    if l >= P[i]:
        mx = max(mx, max_zysk(F, Z, P, l - P[i], i - 1) + Z[i])
    F[l][i] = mx
    return mx


def ogrodnik(T, D, Z, l):
    nd = len(D)
    nt = len(T)
    V = [[False for i in range(len(T[0]))] for j in range(nt)]
    for i in D:
        V[0][i] = True
    P = [poj_drzewa(T, V, x) for x in D]
    F = [[0 for i in range(nd)] for j in range(l + 1)]
    max_zysk(F, Z, P, l, nd - 1)
    return F[l][nd - 1]


runtests(ogrodnik, all_tests=False)
