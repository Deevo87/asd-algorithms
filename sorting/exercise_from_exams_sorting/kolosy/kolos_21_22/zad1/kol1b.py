from kol1btesty import runtests

def split(word):
    n = len(word)
    A = [0 for _ in range(26)]
    for i in range(n):
        A[ord(word[i]) - ord('a')] += 1
    return A

def counting_sort(A, k, index):
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]
    for x in A:
        C[x[index]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i][index]] - 1] = A[i]
        C[A[i][index]] -= 1
    for i in range(n):
        A[i] = B[i]
    return A

def f(T):
    n = len(T)
    maks = 0
    for i in range(n):
        T[i] = split(T[i])
    for ind in range(25, -1, -1):
        maks_int = 0
        for i in range(n):
            maks_int = max(maks_int, max(T[i]))
        counting_sort(T, maks_int+1, ind)
    cnt = 1
    for i in range(1, n):
        if T[i-1] == T[i]:
            cnt += 1
        else:
            maks = max(maks, cnt)
            cnt = 1
    return max(maks, cnt)


from typing import List

"""
Find anagrams. Alorthim starta from changing words to arrays with counter of type of letter. 
This arrays are sorted by radix && counting sort by all 26 letter. Than loop looks for most common word in this sorted 
arrays.
"""


def countingsort(A: List[List[int]], k: int, index: int) -> None:  # stabliny count po kazdym indexie
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i][index]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i][index]] - 1] = A[i]
        C[A[i][index]] -= 1

    for i in range(n):
        A[i] = B[i]


def f2(T: List[str]) -> int:
    n = len(T)
    A = [[0 for _ in range(26)] for _ in range(n)]

    for i in range(n):
        for s in T[i]:
            A[i][ord(s) - 97] += 1

    for i in range(26):
        k = 0
        for j in range(n):
            k = max(A[j][i], k)  # finding k for counting sort

        k += 1
        countingsort(A, k, i)
        for x in A:
            print(x)
        print('[[[[[[[[[[[[[[[[')
    for x in A:
        print(x)
    ans = count = 1
    check = A[0]
    for i in range(1, n):
        if A[i] == check:
            count += 1
        else:
            ans = max(ans, count)
            count = 1
            check = A[i]

    ans = max(ans, count)  # checking last element cuz it never goes to else in loop
    return ans


# if __name__ == '__main__':
#     tab =['tygrys', 'kot', 'wilk', 'trysyg', 'wlik', 'sygryt', 'likw', 'tygrys']
#     print(f(tab))


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
