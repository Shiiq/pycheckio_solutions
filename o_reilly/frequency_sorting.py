# Sort the given list so that its elements end up in the decreasing frequency order,
# that is, the number of times they appear in elements.
# If two elements have the same frequency,
# they should end up according to their natural order.
# For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5].
# If you want to practice more with the similar case, try Sort Array by Element Frequency mission.
# Input: List of integers.
# Output: List or another Iterable (tuple, iterator, generator).
# Examples:
# assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
# assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
#     4,
#     4,
#     4,
#     3,
#     3,
#     11,
#     11,
#     7,
#     13,
# ]
from typing import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    d = [(k, numbers.count(k)) for k in numbers]
    t = sorted(d, key=lambda x: (-x[1], x[0]))
    res = [i[0] for i in t]
    return res


assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [4, 4, 4, 3, 3, 11, 11, 7, 13]
