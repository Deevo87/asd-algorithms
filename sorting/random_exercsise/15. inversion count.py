
def merge(A, B, low, mid, high):
    i = low
    k = low
    j = mid + 1
    count = 0
    for x in range(i, j+1):
        print(A[x])
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            print(A[i], A[j], 'iiiiiiiiiiiiiiiiiiii')
            i += 1
            k += 1
            #count += 1
        else:
            B[k] = A[j]
            print(A[i], A[j])
            j += 1
            k += 1
            count += mid - i + 1
            print(mid, i, count, j)
    while i <= mid:
        B[k] = A[i]
        k += 1
        i += 1
    while j <= high:
        B[k] = A[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        A[i] = B[i]
    return count

def merge_sort(A, B, low, high):
    if low == high:
        return 0
    count = 0
    mid = (low + high) // 2
    count += merge_sort(A, B, low, mid)
    count += merge_sort(A, B, mid + 1, high)
    count += merge(A, B, low, mid, high)
    return count

if __name__ == '__main__':
    X = [1, 9, 6, 4, 5]
    X_zap = [0 for i in range(len(X))]

    print(merge_sort(X, X_zap, 0, len(X)-1))
    print(X)
