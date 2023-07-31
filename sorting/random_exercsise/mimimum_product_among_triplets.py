from queue import PriorityQueue

# Given an integer array, find the minimum product among all combinations of triplets in the array.
# Input:  { 4, -1, 3, 5, 9 }
# Output: The minimum product is -45 (-1, 5, 9)

# O(nlogn) solution - sort array check of negative elements at the start and mutiple them by 2 elements from the end

def findMin(nums):
    n = len(nums)
    min_product = 1
    cnt = 0
    if_negative = min(nums)
    if if_negative > 0:
        min_que = PriorityQueue()
        for x in nums:
            min_que.put(x)
        while not min_que.empty() and cnt != 3:
            cnt += 1
            min_product *= -min_que.get()
        return min_product

    max_que = PriorityQueue()
    for x in nums:
        max_que.put(-x)
    min_product = if_negative
    cnt = 0
    # while not max_que.empty():
    #     print(max_que.get())
    while not max_que.empty() and cnt != 2:
        cnt += 1
        min_product *= -max_que.get()
    return min_product



if __name__ == '__main__':
    tab = [1, 4, 10, -2, 4]
    print(findMin(tab))