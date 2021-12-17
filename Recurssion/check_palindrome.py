def helper(s, si, ei):

    if si >= ei:
        return True
    if s[si] != s[ei]:
        return False

    return helper(s, si+1, ei-1)


def check_palindrome(s):
    si = 0
    ei = len(s) - 1
    return helper(s, si, ei)


s = "abba"
print(check_palindrome(s))
