def binary_search_recurrsion(a, x, si, ei):
    if si > ei:
        return -1

    mid = (si + ei)//2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search_recurrsion(a, x, si, mid-1)

    else:
        return binary_search_recurrsion(a, x, mid+1, ei)


a = [1, 2, 3, 4, 5, 6]

print(binary_search_recurrsion(a, 1, 0, len(a)-1))
