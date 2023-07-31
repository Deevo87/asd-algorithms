# Given a set of intervals, print all non - overlapping intervals after merging the overlapping intervals. For example,
# Input: {1, 5}, {2, 3}, {4, 6}, {7, 8}, {8, 10}, {12, 15}
# Output: Intervals after merging overlapping intervals are
# {1, 6}, {7, 10}, {12, 15}.

def merge(T, low, mid, high):
    B = [0 for _ in range(len(T))]
    i = low
    k = low
    j = mid + 1
    while i <= mid and j <= high:
        if T[i] <= T[j]:
            B[k] = T[i]
            i += 1
            k += 1
        else:
            B[k] = T[j]
            j += 1
            k += 1
    while i <= mid:
        B[k] = T[i]
        i += 1
        k += 1

    while j <= high:
        B[k] = T[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        T[i] = B[i]

def merge_sort(T, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(T, low, mid)
    merge_sort(T, mid + 1, high)
    merge(T, low, mid, high)

#complexity O(nlog), could be O(n) if counting sort was used or queque can be used

def megeIntervals(A):
    n = len(A)
    merge_sort(A, 0, n-1)
    print(A)
    merged_intervals = []
    start = end = 0
    flag = False
    for i in range(1, n):
        if not flag:
            start = A[i - 1][0]
            end = A[i - 1][1]
            flag = True
        if A[i-1][1] >= A[i][0]:
            end = A[i][1]
        else:
            merged_intervals.append([start, end])
            flag = False
    if merged_intervals[len(merged_intervals)-1][1] != A[n-1][1]:
        merged_intervals.append(A[n-1])
    return merged_intervals

if __name__ == '__main__':
    input = [[1, 6], [2, 5], [4, 6], [7, 8], [8, 10], [12, 15]]
    tab = [[1, 2], [3, 4], [5, 6]]
    print(megeIntervals(input))
