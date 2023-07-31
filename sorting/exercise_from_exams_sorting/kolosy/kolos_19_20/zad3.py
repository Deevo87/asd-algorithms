# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba
# z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie
# jak najszybszy. Proszę oszacować jego złożoność obliczeniową.
from math import inf

def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]

def find_sum(T):
    n = len(T)
    counting_sort(T, max(T) + 1)
    for x in T:
        i = 0
        j = n - 1
        flag = False
        while i < j and T[i] < x and T[i] != x:
            suma = T[i] + T[j]
            if suma == x:
                flag = True
                break
            elif suma < x:
                i += 1
            elif suma > x:
                j -= 1
        if not flag:
            return False
    return True

if __name__ == '__main__':
    T = [2, 1, 1, 3, 5, 7, 9, 4, 13, 17, 16]
    print(find_sum(T))