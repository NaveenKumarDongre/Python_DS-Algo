# Subarray with 0 sum in python

# BELOW FIRST 2 FUNCTIONS HAVE THE TIME COMPLEXITY IN O(n**2)
# Using Inbuilt sum
def check_subarray_zero_sum(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(arr[i:j]) == 0:
                return True
    return False

# without using inbuilt function expect range()


def is_zero_sum(arr):
    n = len(arr)
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]

            if(sum_ == 0):
                return True
    return False


# Most efficient solution time complexity O(n)
def is_zero_sum_efficient(arr):
    pre_sum = set()
    sum_ = 0
    for i in arr:
        sum_ = i + sum_
        pre_sum.add(sum_)

        if sum == 0 or sum_ in pre_sum:
            return True

    return False


arr = [4, 3, -2, 1, 1]
print(is_zero_sum(arr))
print(check_subarray_zero_sum(arr))
print(is_zero_sum_efficient(arr))
