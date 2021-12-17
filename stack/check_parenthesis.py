# Check balanced parenthesis

def check_matching(a, b):
    if (a == '[' and b == ']') or (a == '(' and b == ')') or (a == '{' and b == '}'):
        return True
    else:
        return False


def check_balanced_parenthesis(exp):
    stack = []

    for i in exp:

        if i in ('{', '[', '('):
            stack.append(i)

        else:
            if not stack:
                return False
            elif check_matching(stack[-1], i) == False:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True


print("Enter exp:-")
exp = input()
print(check_balanced_parenthesis(exp))
