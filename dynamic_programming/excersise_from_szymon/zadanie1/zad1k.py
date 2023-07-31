from zad1ktesty import runtests


def roznica(S):
    print(S)
    n = len(S)
    A = [0 for _ in range(n)]
    if S[0] == '1':
        A[0] = -1
    else:
        A[0] = 1
    for i in range(1, n):
        if S[i] == '1':
            A[i] = max(A[i], A[i-1] - 1)
        else:
            A[i] = 1
            A[i] = max(A[i], A[i-1] + 1)
    res = max(A)
    if res == 0:
        return -1
    return res



runtests(roznica)
