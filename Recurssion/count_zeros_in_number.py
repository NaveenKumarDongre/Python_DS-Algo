def count_zeros(num):
    if num == 0:
        return 0

    if num % 10 == 0:
        return 1 + count_zeros(num//10)
    else:
        return count_zeros(num//10)


print(count_zeros(0))
