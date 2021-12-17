from typing import Counter


def is_palindrome_per(s):
    # using a inbuilt Cointer method
    cnt = Counter(s)
    # print(cnt)
    odd = 0
    for freq in cnt.values():
        # print(freq)
        if freq % 2 != 0:
            odd = odd + 1
            if odd > 1:
                return False

    return True

# This 2nd function i had done by using dictionaries


def is_palindrome_per_dict(s):
    # making a dictanary count the frequency of the elements
    cnt_freq = dict()
    for i in s:
        if i in cnt_freq:
            cnt_freq[i] += 1
        else:
            cnt_freq[i] = 1
    # print(cnt_freq)
    odd = 0

    for freq in cnt_freq.values():
        # print(freq)
        if freq % 2 != 0:
            odd = odd + 1
            # print(odd)
            if odd > 1:
                return False
    return True


s = "Nav"
print(is_palindrome_per(s))
print(is_palindrome_per_dict(s))
