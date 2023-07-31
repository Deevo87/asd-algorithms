def radix_sort(A):
    n = len(A)
    maks = 0
    for i in range(n):
        maks = max(len(A[i]), maks)
    for i in range(maks - 1, -1, -1):
        A = counting_sort(A, i, 26)
    return A

def counting_sort(A, long, alf):
    n = len(A)
    B = [0]*n
    C = [0]*(alf + 1)
    for x in A:
        if len(x) > long:
            letter = ord(x[long].lower())-96
        else:
            letter = 0
        C[letter] += 1
    for i in range(1, alf):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        if len(A[i]) > long:
            letter = ord(A[i][long].lower())-96
        else:
            letter = 0
        B[C[letter]-1] = A[i]
        C[letter] -= 1
    return B

def group_anagrams(A):
    anagrams = []
    if not A:
        return anagrams
    essa = [''.join(radix_sort(word)) for word in A]
    #print(essa)
    d = {}
    for i, e in enumerate(essa):
        d.setdefault(e, []).append(i)
    for x in d.values():
        collection = tuple(A[i] for i in x)
        #print(x)
        if len(collection) > 1:
            anagrams.append(collection)
    return anagrams


if __name__ == '__main__':
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    tab = ['tygrys', 'kot', 'wilk', 'trysyg', 'wlik', 'sygryt', 'likw', 'tygrys']
    arr = [40870, 11451286, 376607, 1489477, 86738267, 35002, 11451286, 40870, 6222, 376607, 1489477, 6222, 376607,
           35002, 40870, 86738267]
    #print(words)
    print(radix_sort(words))
    print(group_anagrams(words))