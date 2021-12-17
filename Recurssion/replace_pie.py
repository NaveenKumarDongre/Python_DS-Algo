def replace_pi(s):
    l = len(s)
    if(l == 0 or l == 1):
        return s

    if s[0] == 'p' and s[1] == 'i':
        small_output = replace_pi(s[2:])
        return "3.14" + small_output
    else:
        small_output = replace_pi(s[1:])
        return s[0]+small_output


print(replace_pi("abcvdpipifdei"))
