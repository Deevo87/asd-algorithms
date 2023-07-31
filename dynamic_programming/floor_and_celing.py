def binary_search(X, low, high, k):
    n = len(X)
    #if k > X[high]:
       # return -1, X[high]
    #elif k < X[low]:
        #return X[low], -1

    if high >= low:
        mid = (high + low) // 2
        if X[mid] == k:
            return X[mid], X[mid]
        elif X[mid] > k:
            return binary_search(X, low, mid-1, k)
        else:
            return  binary_search(X, mid+1, high, k)
    #print(low, high)
    if high < 0:
        return X[low], -1
    elif low >= n:
        return -1, X[high]
    else:
        return X[low], X[high]


def FandC(X):
    for i in range(11):
        print(binary_search(X, 0, len(X)-1, i), '||', i)


if __name__ == '__main__':
    nums = [1, 4, 6, 8, 9]
    #print(binary_search(nums, 0, len(nums)-1, 10))
    print(FandC(nums))