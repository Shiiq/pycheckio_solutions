# Determine whether the list of elements is ascending
# such that each of its elements is strictly larger
# than (and not merely equal to) the preceding element.
# Empty list consider as ascending.
# Input: A list with integers.
# Output: Boolean.


def is_ascending(items: list[int]) -> bool:
    l = len(items)
    for i in range(l-1):
        if not items[i] < items[i+1]:
            return False
    return True


# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")