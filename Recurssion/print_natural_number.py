def print_1_n(n):
    # base condition when n == 0 i will return
    if n == 0:
        return
    # Recurrsively calling the function
    print_1_n(n-1)
    print(n)


def print_1_n_reverse(n):
    if n == 0:
        return
    print(n)
    print_1_n_reverse(n-1)


print_1_n_reverse(10)
