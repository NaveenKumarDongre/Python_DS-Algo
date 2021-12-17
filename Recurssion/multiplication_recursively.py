# one twist is here that you should not use "*"
# operator u can use + or -

def multiple(n, m):

    if m == 0:
        return 0
    small_output = multiple(n, m-1)
    return n+small_output


print(multiple(5, 5))
