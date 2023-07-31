import sys

def max_prod(nums):
    n = len(nums)
    max_1 = max_2 = -sys.maxsize
    min_1 = min_2 = sys.maxsize
    for x in nums:
        if x > max_1:
            max_2 = max_1
            max_1 = x
        if x < min_1:
            min_2 = min_1
            min_1 = x
    if min_2 * min_1 > max_2 * max_2:
        return min_1, min_2
    return max_1, max_2

if __name__ == '__main__':
    A = [-10, -3, 5, 6, -2]
    print(max_prod(A))