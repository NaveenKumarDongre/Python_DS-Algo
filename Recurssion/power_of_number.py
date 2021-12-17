def power_of_number(num, power):
    # Base codition is when power is 0
    if power == 0:
        return 1

    return num * power_of_number(num, (power-1))


print(power_of_number(2, 5))
