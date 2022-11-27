# You have a sequence of strings, and you’d like to determine
# the most frequently occurring string in the sequence. It can be only one.
# Input: non empty list of strings.
# Output: a string.
# Examples:
# assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
# assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
from functools import reduce

DATA = ["a", "b", "c", "a", "b", "a"]


def most_frequent(data: list[str]) -> str:
    d = {}
    for i in data:
        if i not in d:
            d[i] = 1
        d[i] += 1
    # {'a': 4, 'b': 3, 'c': 2}
    s = tuple(d.items())
    # (('a', 4), ('b', 3), ('c', 2))
    res = reduce(lambda a, b: a if (a[1] > b[1]) else b, s)
    return res[0]


assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
