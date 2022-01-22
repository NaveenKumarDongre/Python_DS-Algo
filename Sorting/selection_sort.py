# Selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
