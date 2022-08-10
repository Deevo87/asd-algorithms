from zad2ktesty import runtests

def palindrom( S ):
    n = len(S)
    S2 = S[::-1]
    A = [[0 for _ in range(n+1)] for _ in range(n+1)]
    ending = n
    maxlength = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if S[i-1] == S2[j-1]:
                A[i][j] = A[i-1][j-1] +1
            if maxlength < A[i][j]:
                maxlength = A[i][j]
                ending = i
    return S[ending-maxlength:ending]

runtests ( palindrom )