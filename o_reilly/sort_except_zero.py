# Sort the integers in a list. But the position of zeros should not be changed.
# Input: A list of integers.
# Output: A list or another Iterable (tuple, generator, iterator) of integers.
# Examples:
# assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
# assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
# assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
from typing import Iterable


def except_zero(items: list) -> Iterable:
    pass

DATA = [5, 3, 0, 0, 4, 1, 4, 0, 7]
var_1 = sorted(DATA)
var_2 = sorted(DATA, key=lambda x: x==0)
var_3 = sorted(DATA, key=lambda x: x!=0)

print(var_1)
print(var_2)
print(var_3)