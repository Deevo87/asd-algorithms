#Rafał Laskowski

'''
    Najpierw sortuje tablicę S algorytmem quick sort (rosnąco) następnie do momentu, aż w wąwozie pojawi się pierwsze 0
    wychodzę z pętli i zwracam poprawny wynik.
    Pomijam fakt wsochdniej i zachodniej bramy, ponieważ zawsze i tak będę wybierał największe możliwe wartości z tablicy.
    Dlatgo nawet jeżeli największe wartości byłyby na samym środku to wyjdzie na to samo, ponieważ kolejność zbierania
    śniegu nie ma znaczenia.
'''

from zad2testy import runtests

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] > x:
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
    j = 0
    for i in range(n-1, -1, -1):
        A[j] = B[i]
        j += 1

def snow( S ):
    n = len(S)
    quick_sort(S, 0, n-1)
    # counting_sort(S, max(S)+1)
    days = 0
    result = 0
    for i in range(n):
        if S[i] - days > 0:
            result += S[i] - days
        else:
            break
        days += 1
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
