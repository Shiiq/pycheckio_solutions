# You are given a list of integers, which are elements of arithmetic progression -
# the difference between the consecutive elements is constant.
# But this list is unsorted and one element is missing...good luck!
# Input: List of integers.
# Output: Integer.
# Examples:
# assert missing_number([1, 4, 2, 5]) == 3
# assert missing_number([2, 6, 8]) == 4
from functools import reduce
DATA = [1, 4, 2, 5]
# [1, 2, 4, 5]
DATA.sort()
DATA.reverse()
# min_dif = ([(DATA[i] - DATA[i+1]) for i in range(len(DATA)-1)])
for i in range(len(DATA)-1):
    d = DATA[i+1] - DATA[i]



# def missing_number(items: list[int]) -> int:
    # return 0