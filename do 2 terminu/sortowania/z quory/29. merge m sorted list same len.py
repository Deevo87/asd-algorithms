import pathlib


def left_ind(A, i):
    n = len(A)
    parent = n-i-1
    return n - (2*parent + 2) - 1

def right_ind(A, i):
    n = len(A)
    parent = n-i-1
    return n - (2*parent + 1) - 1

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def heapify(A, n, i): #dziwny heap z wyszukiwaniem parenta (?)
    l = left_ind(A, i)
    r = right_ind(A, i)
    maks_ind = i
    if l >= 0 and A[l][0] > A[maks_ind][0]:
        maks_ind = l
    if r >= 0 and A[r][0] > A[maks_ind][0]: #max heap
        maks_ind = r
    if maks_ind != i:
        swap(A, maks_ind, i)
        heapify(A, n, maks_ind)

def heap_maker(A):
    n = len(A)
    parent = 0
    while parent < n:
        heapify(A, n, parent)
        parent += 1

def merge_m_lists(lists):
    n = len(lists)
    index = [len(lists[i])-1 for i in range(n)]
    lenght = 0
    for i in range(n):
        lenght += len(lists[i])
    output = [0] * lenght
    count = lenght - 1
    A = []
    for i in range(n):
        A.append((lists[i][index[i]], i))
        index[i] -= 1
    heap_maker(A)
    while count >= 0:
        x = A.pop()
        print(count)
        output[count] = x[0]
        count -= 1
        if index[x[1]] > -1:
            A.append((lists[x[1]][index[x[1]]], x[1]))
            index[x[1]] -= 1
        heapify(A, n, len(A)-1)
    return output


if __name__ == '__main__':
    tab1 = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
        [16, 18, 22, 28]
    ]
    print(merge_m_lists(tab1))
