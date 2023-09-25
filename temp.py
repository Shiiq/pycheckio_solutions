from itertools import islice
from functools import reduce

# a = [1, 2, 3, 4, 5, 6]
# iterator = iter(a)
# list(iter(lambda: list(islice(iterator, 3)), []))

# print(list(islice(iterator, 3)))

data = "design, and sometimes because of a bug in the code that prepared these iterables"
abc = "abcdefghijklmnopqrstuvwxyz"



clear_data = data.strip().replace(",", "").split()
# ['design', 'and', 'sometimes', 'because', 'of', 'a', 'bug', 'in', 'the', 'code', 'that', 'prepared', 'these', 'iterables']

weigths = {s: w for w, s in enumerate(abc, start=1)}
short_result = max([sum(weigths[sym] for sym in word) for word in data.strip().replace(",", "").split()])
print(short_result)

matrix = [
    (1, 2, 3),
    ("a", "b", "c")
]
t_matrix = [
    (1, "a"),
    (2, "b"),
    (3, "c")
]

t_m = list(zip(*matrix))

assert t_m == t_matrix
