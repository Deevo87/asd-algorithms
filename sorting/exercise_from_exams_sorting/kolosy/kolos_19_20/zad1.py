# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

def take_num_len(num):
    cnt = 0
    while num != 0:
        num // 10

def count(num):
    single = 0
    many = 0
    C = [0 for _ in range(10)]
    tmp = num
    maks = 0
    while tmp != 0:
        digit = tmp % 10
        tmp //= 10
        C[digit] += 1
        maks += 1
    for i in range(10):
        if C[i] == 1:
            single += 1
        elif C[i] > 1:
            many += 1
    return num, single, many

def compute_longest_num(T):
    maks = max(T)
    cnt = 0
    while maks != 0:
        maks //= 10
        cnt += 1
    return cnt

def radix_sort(A, k):
    n = len(A)
    for i in range(2, 0, -1):
        A = counting_sort(A, k, i)
    return A

def counting_sort(A, k, pos):
    n = len(A)
    B = [0 for _ in range(n)]
    C = [0 for _ in range(k)]
    for x in A:
        C[x[pos]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i][pos]]-1] = A[i]
        C[A[i][pos]] -= 1
    for i in range(n-1, -1, -1):
        A[n-i-1] = B[i]
    return A

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j][1] > x[1]:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j][1] == x[1]:
            if A[j][2] < x[2]:
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

def pretty_sort(T):
    n = len(T)
    A = [(0, 0, 0) for _ in range(n)]
    maks = compute_longest_num(T)
    for i in range(n):
        A[i] = count(T[i])

    A = radix_sort(A, maks)
    # quick_sort(A, 0, n-1)

    return A

if __name__ == '__main__':
    # print(count(1332))
    tab = [123, 445, 28, 22, 4456]
    print(pretty_sort(tab))
