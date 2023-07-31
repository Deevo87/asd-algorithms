from zad3testy import runtests
import sys
sys.setrecursionlimit(10000)

def radix_sort_str(A):
    n = len(A)
    maks = 0
    for i in range(n):
        maks = max(len(A[i]), maks)
    for i in range(maks - 1, -1, -1):
        A = counting_sort_for_str(A, i, 26)
    return A

def counting_sort_for_str(A, long, alf):
    n = len(A)
    B = [0]*n
    C = [0]*(alf + 1)
    for x in A:
        if x != 0 and len(x) > long:
            letter = ord(x[long].lower())-96
        else:
            letter = 0
        C[letter] += 1
    for i in range(1, alf+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        if len(A[i]) > long:
            letter = ord(A[i][long].lower())-96
        else:
            letter = 0
        B[C[letter]-1] = A[i]
        C[letter] -= 1
    return B

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        #quick_sort(A, q + 1, r)
        p = q + 1

def strong_string(T):
    n = len(T)
    maks = 0
    for x in T:
        maks = max(len(x), maks)

    buckets = [[] for _ in range(maks+1)]
    for x in T:
        buckets[len(x)].append(x)
        if x[::-1] != x:
            buckets[len(x)].append(x[::-1])

    for i in range(maks):
        # buckets[i] = radix_sort_str(buckets[i])
        if buckets[i] is not None:
            buckets[i].sort()
            if i > 5:
                quick_sort(buckets[i], 0, len(buckets[i])-1)
            else:
                buckets[i] = radix_sort_str(buckets[i])

    most_popular = 0
    for i in range(maks):
        cnt = 1
        for j in range(len(buckets[i])-1):
            if buckets[i][j] == buckets[i][j+1]:
                cnt += 1
                most_popular = max(most_popular, cnt)
            else:
                cnt = 1
    return most_popular


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
