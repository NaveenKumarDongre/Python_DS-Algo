def sum_of_list(a, si):
    l = len(a)
    if si == l:
        return 0
    return a[si]+sum_of_list(a, si+1)


def is_number_present(a, x, si):
    l = len(a)

    if si == l:
        return False
    if a[si] == x:
        return True

    return is_number_present(a, x, si+1)


a = [3, 3, 3]
print(sum_of_list(a, 0))
print(is_number_present(a, 1, 0))
