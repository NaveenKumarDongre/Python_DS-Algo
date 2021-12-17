
def factorial(n):
    # Base condition n==0
    if n == 0:
        return 1
    return n*factorial(n-1)


def find_nth_fibonacci(n):
    # find_nth_fibonacci(1) = 1
    if n == 1:
        return 1
    if n == 2:
        return 1

    return find_nth_fibonacci(n-1)+find_nth_fibonacci(n-2)


print(factorial(4))
print(find_nth_fibonacci(4))
