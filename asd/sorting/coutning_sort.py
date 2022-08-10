from random import randint

def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    #C = [0 for _ in range(n)]
    #B = [0 for _ in range(n)]
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]

if __name__ == '__main__':
    test = [randint(0, 100) for i in range(100)]
    print(test)
    counting_sort(test, 101)
    print(test)