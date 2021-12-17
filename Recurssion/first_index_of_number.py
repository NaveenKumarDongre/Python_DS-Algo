def find_first_index(a, x):
    l = len(a)
    if l == 0:
        return -1
    if a[0] == x:
        return 0
    smaller_list = a[1:]
    smaller_list_output = find_first_index(smaller_list, x)

    if smaller_list == -1:
        return -1
    else:
        return smaller_list_output + 1


def find_first_index_better(a, x, si):
    l = len(a)
    if si == l:
        return -1
    if a[si] == x:
        return si
    smaller_list_ouput = find_first_index_better(a, x, si+1)
    if smaller_list_ouput == -1:
        return -1
    else:
        return smaller_list_ouput


a = [1, 2, 3, 7, 7, 8]

print("Output", find_first_index_better(a, 100, 0))
