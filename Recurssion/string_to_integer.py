def string_to_integer(s, si):

    if si == 0:
        return 0
    small_answer = string_to_integer(s, si - 1)
    next_digit = ord(s[len(s) - 1]) - ord('0')
    final_answer = (small_answer*10) + next_digit
    return final_answer


print(string_to_integer("1234", 4))
print("Hello World")
