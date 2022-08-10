def prime_checker(a):
    if a < 2:
        return False
    if a == 2 or a == 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4
    return True

def prime_generator(n):
    cnt = 0
    primes = [0 for _ in range(n)]
    a = 2
    while cnt < n:
        if prime_checker(a):
            primes[cnt] = a
            cnt += 1
        a += 1
    return primes

def radix_sort(A):
    maks = max(A)
    i = 1
    while maks / i > 1:
        counting_sort(A, i)
        i *= 10


def counting_sort(A, k):
    n = len(A)
    B = [0] * n
    C = [0] * 10 #jest 10 cyfr
    for x in A:
        ind = x // k
        C[ind%10] += 1
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        ind = A[i] // k
        B[C[ind%10]-1] = A[i]
        C[ind%10] -= 1
    for i in range(n):
        A[i] = B[i]
    return B


def f(A):
    n = len(A) #ilość napisów
    b = 26 #ilość liter w alfabecie
    syg = [1 for _ in range(n)]
    primes = prime_generator(b)
    for cnt, x in enumerate(A):
        length = len(x) - 1
        while length >= 0:
            syg[cnt] *= primes[ord(x[length].lower()) - 97]
            length -= 1
    cnt = 0
    last = -1
    maks = -1
    radix_sort(syg)
    print(syg)
    for i in range(n):
        if last == syg[i]:
            cnt += 1
            print(syg[i], cnt)
        else:
            last = syg[i]
            maks = max(cnt, maks)
            cnt = 1
    maks = max(maks, cnt)
    return maks


if __name__ == '__main__':
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    tab = ['tygrys', 'kot', 'wilk', 'trysyg', 'wlik', 'sygryt', 'likw', 'tygrys']
    arr = [40870, 11451286, 376607, 1489477, 86738267, 35002, 11451286, 40870, 6222, 376607, 1489477, 6222, 376607,
           35002, 40870, 86738267]
    tab2 = ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']
    print(f(tab2))