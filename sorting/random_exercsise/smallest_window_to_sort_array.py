# Given an integer array, find the smallest window sorting which will make the entire array sorted in increasing order.
import sys


def window(nums):
    if not nums:
        return None

    n = len(nums)
    if sum(nums) < 0:
        tmp = [0 for _ in range(n)]
        for i in range(1, n):
            print(nums[n-i], n-i)
            tmp[i] = abs(nums[n-i])
        nums = tmp
    print(nums)
    start = -1
    end = -1
    for i in range(n-1):
        if nums[i] >= nums[i + 1]:
            start = i
            break

    for i in range(n-1, start, -1):
        if nums[i - 1] > nums[i]:
            end = i
            break

    if end == -1 or start == -1:
        return None

    return start, end

def window2(nums):
    n = len(nums)

    if not nums:
        return None

    start = -1
    end = -1
    print(start, end)
    maks = -sys.maxsize
    mini = sys.maxsize
    for i in range(n):
        if maks < nums[i]:
            maks = nums[i]

        if maks > nums[i]:
            end = i

    for i in range(n-1, -1, -1):
        if mini > nums[i]:
            mini = nums[i]

        if mini < nums[i]:
            start = i
    print(start, end)
    if start == -1:
        return None

    return start, end

if __name__ == '__main__':
    tab = [8, 7, 6, 5, 4, 3, 2, 1]
    print(window2(tab))