def sum_natural_num(n):
    #  Base Codition is n==0
    if n == 0:
        return 0
    return n+sum_natural_num(n-1)


print(sum_natural_num(11))
