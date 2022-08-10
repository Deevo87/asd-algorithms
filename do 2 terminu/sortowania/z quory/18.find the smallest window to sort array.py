def find_sublist(nums):
    n = len(nums)
    start = -1
    end = -1
    sm = max(nums) + 1
    sm_ind = -1
    for i in range(n-1):
        if nums[i] > nums[i+1] and start < 0:
            start = i
        if nums[i] > nums[i+1]:
            end = -1
            if sm > nums[i+1]:
                sm = nums[i+1]
                sm_ind = i+1
        if end < 0 and nums[i] < nums[i+1]:
            end = i
    if start-1 >= 0 and nums[start-1] > sm:
        start = start-1
    if start < 0:
        return None
    if end < 0:
        end = n-1
    return start, end
#fajne i proste rozwiązanie jest na techiedelight szukam max i min i tyle tak naprwdę
if __name__ == '__main__':
    tab = [1, 2, 3, 5, 4, 6, 7, 8]
    print(find_sublist(tab))