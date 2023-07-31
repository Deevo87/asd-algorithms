from random import randint


def counting_sort(A, k):
    n = len(A)
    # C = [0] * k
    # B = [0] * n
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]
    for x in A:
        C[k(x)] += 1
    for i in range(1, n):
        C[i] = C[i] + C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[k(A[i])] - 1] = A[i]
        C[k(A[i])] -= 1
    for i in range(n):
        A[i] = B[i]
    return A


def radix_sort_int(A):
    n = len(A)
    sortd = counting_sort(A, lambda x: x % n)
    return counting_sort(sortd, lambda x: x // n)


def radix_sort_str(A):
    n = len(A)
    maks = 0
    for i in range(n):
        maks = max(len(A[i]), maks)
    for i in range(maks - 1, -1, -1):
        A = counting_sort_for_str(A, i, 26)
    return A

def counting_sort_for_str(A, long, alf):
    n = len(A)
    B = [0]*n
    C = [0]*(alf + 1)
    for x in A:
        if x != 0 and len(x) > long:
            letter = ord(x[long].lower())-96
        else:
            letter = 0
        C[letter] += 1
    for i in range(1, alf + 1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        if len(A[i]) > long:
            letter = ord(A[i][long].lower())-96
        else:
            letter = 0
        B[C[letter]-1] = A[i]
        C[letter] -= 1
    return B



if __name__ == '__main__':
    test = [randint(0, 100 ** 2) for i in range(100)]
    #print(radix_sort_int(test1))
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    test3 = ['kra', 'art', 'kot', 'kit', 'ati', 'kil', 'aaaa', 'abcabcabc']
    print(radix_sort_str(['w', 'i', 'l', 'k']))
