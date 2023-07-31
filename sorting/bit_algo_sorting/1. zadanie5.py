#złożoność O(n)

def counting_sort(A, k):
    n = len(A) - 10
    B = [0]*n
    C = [0]*k
    for x in A:
        if x is not None:
            C[x] += 1
    print(C)
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n+9, -1, -1):
        if A[i] is not None:
            print(A[i])
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
    return B

def zad5(A, k):
    n = len(A)
    lower = []
    bigger = []
    for i in range(n):
        if A[i] > k:
            bigger.append(A[i])
            A[i] = None
        elif A[i] < 0:
            lower.append(A[i])
            A[i] = None
    bigger.sort()
    lower.sort()
    main = counting_sort(A, k)
    for i in range(len(bigger)):
        main.append(bigger[i])
    for i in range(len(lower)-1, -1, -1):
        main.insert(0, lower[i])
    for i in range(n):
        A[i] = main[i]

if __name__ == '__main__':
    tab = [-10000, -90000, -888, -111111, 25, 12, 4, 6, 32, 17, 29, 22, 33, 11, 8, 19, 12, 100000, 9999999, 2222, 3333, 111, 999]
    zad5(tab, 35)
    print(tab)
