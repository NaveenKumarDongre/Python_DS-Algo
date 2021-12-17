def find_last_index(a, x):

    l = len(a)
    if l == 0:
        return -1
    smaller_list = a[1:]
    smaller_list_output = find_last_index(smaller_list, x)

    if smaller_list_output != -1:
        return smaller_list_output + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1


def find_last_index_better(a, x, si):

    l = len(a)

    if si == l:
        return -1
    smaller_list_output = find_last_index_better(a, x, si+1)

    if smaller_list_output != -1:
        return smaller_list_output
    else:
        if a[si] == x:
            return si
        else:
            return -1


a = [1, 2, 3, 3, 5, 6, 6, 6, 6]
print(find_last_index_better(a, 6, 0))
