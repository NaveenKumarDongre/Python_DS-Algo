def is_sorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    if a[0] > a[1]:
        return False
    smaller_list = a[1:]
    is_smaller_list_sorted = is_sorted(smaller_list)

    if is_smaller_list_sorted:
        return True
    else:
        return False


def is_sorted_better(a, si):
    l = len(a)
    if si == l-1 or si == l:
        return True
    if a[si] > a[si + 1]:
        return False
    is_smaller_part_sorted = is_sorted_better(a, si + 1)

    return is_smaller_part_sorted


a = [1, 2, 3, 400, -1, 6, 7, 8]
print("Output", is_sorted_better(a, 0))
