from math import sqrt

def zad10(A):
    n = len(A)
    C = [0]*(int(sqrt(n))+1)
    for i in range(2, len(C)):
        for j in range(n):
            if A[j] % i == 0:
                C[i] += 1
    return max(C)


if __name__ == '__main__':
    tab = [2, 4, 6, 8, 10, 3, 9, 6, 12]
    print(zad10(tab))
