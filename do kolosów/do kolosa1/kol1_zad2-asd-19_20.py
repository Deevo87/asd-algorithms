from random import randint

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1



def q_select(A, low, high, ind):
    if low == ind:
        return A[low]
    if low < high:
        q = partition(A, low, high)
        if q == ind:
            return A[q]
        elif q < ind:
            return q_select(A, q+1, high, ind)
        else:
            return q_select(A, low, q-1, ind)


def section(T, p, q):
    p_val = q_select(T, 0, q, p)
    q_val = q_select(T, p, len(T)-1, q)
    print(p_val, q_val)
    #print(T)
    for i in range(p, q+1):
        print(T[i], end=', ')

if __name__ == '__main__':
    T = [(randint(1700, 2000)/1000) for _ in range(10)]
    print(T)
    pp = 1
    qq = 7
    section(T, pp , qq)
    print('\n')
    quick_sort(T, 0, len(T)-1)
    print(T)