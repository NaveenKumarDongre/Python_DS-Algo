# merging two sorted subarrays

def merge_two_sorted_array(a, b):
    m = len(a)
    n = len(b)
    res = []
    i, j = 0, 0

    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < m:
        res.append(a[i])
        i += 1

    while j < n:
        res.append(b[j])
        j += 1

    return res


def merge_sorted_subarrays(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


a = [10, 15, 20, 40, 8, 11, 55]

low = 0
mid = 3
high = 6

merge_sorted_subarrays(a, low, mid, high)

print(a)
