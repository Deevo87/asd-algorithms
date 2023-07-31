def partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r):
        if A[j][1] <= x:
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

def selection(activities):
    if not activities:
        return None
    n = len(activities)
    quick_sort(activities, 0, n - 1)
    print(activities)
    result = [activities[0]]
    j = 0
    for i in range(1, n):
        if activities[i][0] >= result[j][1]:
            result.append(activities[i])
            j += 1
    return result

if __name__ == '__main__':
    tab = [(3, 7), (1, 3), (2, 9), (2, 7), (1, 2), (7, 8)]
    print(selection(tab))