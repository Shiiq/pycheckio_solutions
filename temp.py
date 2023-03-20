from itertools import islice
from functools import reduce

# a = [1, 2, 3, 4, 5, 6]
# iterator = iter(a)
# list(iter(lambda: list(islice(iterator, 3)), []))

# print(list(islice(iterator, 3)))

# DATA = [1, 2, 4, 5, 6, 7, 8]
DATA = [1, 3, 7]
d = {
    #"diff": "frequency",
}

l = len(DATA) - 1
dif = DATA[1] - DATA[0]
for i in range(l):
    cur = DATA[i]
    nxt = DATA[i+1]
    cur_dif = nxt - cur
    if dif > cur_dif:
        dif = cur_dif
    # diff = nxt - cur
    # print(i) if diff == 2 else None
    # d[diff] = d.setdefault(diff, 0) + 1

# print(d)
# m_d = min(d.items(), key=lambda x: x[0])[0]
# main_diff = max(d.items(), key=lambda x: x[1])[0]
# sec_diff = min(d.items(), key=lambda x: x[1])[0]
start = DATA[0]
last = DATA[l]
from_start = [i for i in range(start, last+dif, dif)]
# print(from_start)
# from_last = [i for i in range(last, start-m_d, -m_d)]
# print(from_last)
dig = sum(from_start) - sum(DATA)
print(dig)
