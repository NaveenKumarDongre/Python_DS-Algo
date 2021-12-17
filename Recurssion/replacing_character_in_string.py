def replace_char(s, a, b):
    if len(s) == 0:
        return s
    small_output = replace_char(s[1:], a, b)
    if s[0] == a:
        return b + small_output
    else:
        return s[0]+small_output


print(replace_char("aaabxyb", 'a', 'b'))
