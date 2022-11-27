# assert sum_digits(38) == 2
# assert sum_digits(0) == 0
# assert sum_digits(10) == 1
# assert sum_digits(132) == 6


def sum_digits(num: int) -> int:
    if num < 10:
        return num
    list_int = [int(i) for i in str(num)]
    num = sum(list_int)
    return sum_digits(num)


assert sum_digits(38) == 2
assert sum_digits(0) == 0
assert sum_digits(10) == 1
assert sum_digits(132) == 6
