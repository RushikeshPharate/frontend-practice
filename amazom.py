


def is_lex_reversed_small(lst):
    left, right = 0, len(lst) - 1
    # print(lst)
    while left < right:
        if lst[right] < lst[left]:
            left += 1
            right -= 1
        else:
            return False
    return True


def return_count(s, k):
    n = len(s)
    s_list = list(s)
    i = 0
    count = 0
    while i < n - k + 1:
        if is_lex_reversed_small(s_list[i : i + k]):
            count += 1
        i += 1
    return count

print(return_count("amazon", 3)) 
print(return_count("ababa", 2)) 
print(return_count("aaaa", 4)) 