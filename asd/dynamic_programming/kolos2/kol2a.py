from kol2atesty import runtests

def drivers( P, B ):
    n = len(P)
    P.sort(key=lambda Z:Z[0])
    print(P)
    cnt = 0 # ilość punktów kontrolnych dla każego punktu przesiadkowego
    PRZE = []
    for i in range(n):
        if P[i][1]:
            PRZE.append(cnt)
            cnt = -1
        cnt += 1
    return []

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )