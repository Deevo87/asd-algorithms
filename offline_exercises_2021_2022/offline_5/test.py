from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    k = T[0][0]
    i, cnt = 1, 0
    A = [T[0][1]]
    q = PriorityQueue()
    while i < n-1:
        q.put((-T[i][0], T[i][1]))
        cnt += 1
        if cnt == k:
            item = q.get()
            A.append(item[1])
            k = k - abs(T[i-k][1] - item[1]) - item[0]
            cnt = 0
            i = item[1]
        i += 1
    A.sort()
    return A

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )