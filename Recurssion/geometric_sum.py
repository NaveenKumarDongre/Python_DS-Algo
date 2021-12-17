def geometric_sum(k):

    if k == 0:
        return 1
    small_output = geometric_sum(k-1)
    return ((1/2)**k)+small_output


print(geometric_sum(3))
