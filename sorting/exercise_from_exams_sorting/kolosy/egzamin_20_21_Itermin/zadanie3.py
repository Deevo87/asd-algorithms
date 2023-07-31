# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a
# x
# , gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
# obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
from Exercise_1_tests import runtests

from zad3testy import runtests
from math import log


def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

def fast_sort(A, a):
    b = 10  # ilość bucketów, wiem bo ile ich jest bo rozkład jest na [0, 1]
    C = [[] for _ in range(b)]
    for x in A:
        C[int(log(x, a)*b)].append(x)  # bucket_index = (max-min)/n
    #print(C)
    for i in C:
        if len(i) != 0:
            insertion_sort(i)
    cnt = 0
    for i in C:
        tmp = len(i)
        ind = 0
        while ind < tmp:
            A[cnt] = i[ind]
            cnt += 1
            ind += 1
    return A

runtests(fast_sort)

# if __name__ == '__main__':
#     T = [0, 2, 1.1, 2]