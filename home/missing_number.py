# You are given a list of integers, which are elements of arithmetic progression -
# the difference between the consecutive elements is constant.
# But this list is unsorted and one element is missing...good luck!
# Input: List of integers.
# Output: Integer.
# Examples:
# assert missing_number([1, 4, 2, 5]) == 3
# assert missing_number([2, 6, 8]) == 4
# assert missing_number([2, 4, 6, 10]) == 8

def missing_number(items: list[int]) -> int:
    items.sort()
    l = len(items) - 1
    dif = items[1] - items[0]
    for i in range(l):
        cur = items[i]
        nxt = items[i + 1]
        cur_dif = nxt - cur
        if dif > cur_dif:
            dif = cur_dif
    start = items[0]
    last = items[l]
    from_start = [i for i in range(start, last + dif, dif)]
    dig = sum(from_start) - sum(items)
    return dig

print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

# разобрать решение
# def missing_number(items: list[int]) -> int:
#     i = 0
#     while True:
#         test = [x for x in items]
#         test.append(i)
#         test.sort()
#         diffs = [test[x+1]-test[x] for x in range(len(test)-1)]
#         if len(set(diffs)) == 1:
#             return i
#         i += 1