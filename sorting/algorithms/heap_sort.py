def left_ind(i):
    return 2 * i + 2


def right_ind(i):
    return 2 * i + 1


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def heapify(A, i, n):
    left = left_ind(i)
    right = right_ind(i)
    maks_ind = i
    if left < n and A[maks_ind] < A[left]: #teraz jest max-heap
        maks_ind = left
    if right < n and A[maks_ind] < A[right]:
        maks_ind = right
    if maks_ind != i:
        swap(A, i, maks_ind)
        heapify(A, maks_ind, n)


def pop(A, n): # sciąganie z kopca
    if n <= 0:
        return -1
    top = A[0]
    A[0] = A[n - 1]
    heapify(A, 0, n - 1)
    return top

def insert(A, x):
    A.append(x)
    child = len(A) - 1
    parent = (child-1)//2
    while child > 0 and A[parent] < A[child]:
        A[parent], A[child] = A[child], A[parent]
        child = parent
        parent = child//2

def heap_sort(A):
    n = len(A)
    parent = (n-2)//2
    while parent >= 0:
        heapify(A, parent, n)
        parent -= 1
    while n > 0:
        A[n - 1] = pop(A, n)
        n -= 1

if __name__ == '__main__':
    tab = [8, 2, 4, 5, 1, 2, 6, 12]
    print(tab)
    heap_sort(tab)
    print(tab)
    insert(tab, 13)
    print(tab)
    heap_sort(tab)
    print(tab)
    #insert(tab, 13)
    #heap_sort(tab)
    #print(tab)