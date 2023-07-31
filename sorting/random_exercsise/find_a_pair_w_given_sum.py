#Given an unsorted integer array, find a pair with the given sum in it. O(n)/O(nlogn)


def counting_sort(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]

def findPair(nums, target):
    n = len(nums)
    i = 0
    j = n-1
    counting_sort(nums, max(nums)+1)
    while  i < j:
        if nums[i] + nums[j] == target:
            return nums[i], nums[j]

        if nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return None

if __name__ == '__main__':
    A = [5, 2, 6, 8, 1, 9]
    print(findPair(A, 10))