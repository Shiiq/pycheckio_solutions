# You are given a list of integers. Your task in this mission is to find,
# how many times the sorting direction was changed in the given list.
# If the elements are equal - the previous sorting direction remains the same,
# if the sequence starts from the same elements - look
# for the next different to determine the sorting direction.

# def changing_direction(elements: list[int]) -> int:
    # l = len(elements)
    # c = 0
    # start_direction = None
    # for i in range(l-2):
    #     cur = elements[i]
    #     next = elements[i+1]
    # return 0


# These "asserts" are used for self-checking
# assert changing_direction([1, 2, 3, 4, 5]) == 0
# assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
# print("The mission is done! Click 'Check Solution' to earn rewards!")
