from zad3ktesty import runtests


def ksuma(T, k):
    print(T, k)
    tmp = max(T)
    mini = tmp
    n = len(T)
    A = [mini for _ in range(n)]
    cnt = 1
    suma = 0
    for i in range(k):
        mini = min(mini, T[i])
    A[0] = mini
    for i in range(1, n - k + 1):
        if cnt == k:
            cnt = 1
            suma += mini
            mini = tmp
        for j in range(k-1):
            if i + k - 1 >= n - 1:
                if cnt != 1:
                    suma += mini
                    mini = tmp
                cnt = 1
                mini = min(mini, T[i + j])
            elif cnt == 1:
                mini = min(mini, T[i + j])
            elif mini > T[i + j]:
                mini = min(T[i + j], A[i - 1])
        cnt += 1
        A[i] = mini
    suma += mini
    return suma


runtests(ksuma)
