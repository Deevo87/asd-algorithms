import time
from random import randint
start_time = time.time()

#jakiś kod

print("--- %s seconds ---" % (time.time() - start_time))



def max_expr(A):
    n = len(A)
    X = [0 for _ in range(n)]
    res = 0
    mini = A[0]
    indmi = 0
    indma = 0
    #print(mini)
    maks = min(A) - 1
    for i in range(n-3):
        if mini > A[i]:
            mini = A[i]
            indmi = i

    res -= mini
    for i in range(indmi+1, n-2):
        if maks < A[i]:
            maks = A[i]
            indma = i
    res += maks
    mini = max(A) + 1
    for i in range(indma+1, n-1):
        if mini > A[i]:
            mini = A[i]
            indmi = i
    res -= mini
    maks = min(A) - 1
    for i in range(indmi+1, n):
        if maks < A[i]:
            maks = A[i]
    res += maks
    return res


if __name__ == '__main__':
    A = [3, 9, 10, 1, 30, 40]
    B = [randint(1, 100) for _ in range(1000000)]
    print(B)
    print(max_expr(B))
    print("--- %s seconds ---" % (time.time() - start_time))