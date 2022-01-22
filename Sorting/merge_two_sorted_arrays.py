# Merge two sorted arrays


# Navie Solution
def merge(a, b):
    res = a + b
    res.sort()
    return res


def merge_2_sorted_list(a, b):
    m, n = len(a), len(b)
    i, j = 0, 0
    ans = []

    while i < m and j < n:
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1
    while i < m:
        ans.append(a[i])
        i += 1
    while j < n:
        ans.append(b[i])
        j += 1
    return ans


a = [1, 5, 10]
b = [0, 2, 6, 9]
res = merge_2_sorted_list(a, b)
print(res)
