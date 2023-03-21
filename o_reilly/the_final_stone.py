# You have a list of stones with different weights.
# The result of hitting two stones will be a new stone
# with a weight difference between the two stones.
# Your goal is to find the weight of the final stone. If no stones left, the result is 0.
# The algorith is very simple:
# get the two biggest stones in the batch
# hit and get the resulting stone
# put the resulting stone back in the batch.
# For the Speedy category, you can think about your solution for a million stones


def final_stone(stones: list[int]) -> int:
    if not stones:
        return 0
    cursor = len(stones)
    if cursor == 1:
        return 1
    stones.sort()
    while cursor > 2 :
        max_1 = stones.pop()
        max_2 = stones.pop()
        dif = abs(max_1 - max_2)
        stones.append(dif)
        cursor -= 1
    num_1, num_2 = stones
    dif = abs(num_1 - num_2)
    return dif


print('Example:')
print(final_stone([1,2,3]))

assert final_stone([3, 5, 1, 1, 9]) == 1
assert final_stone([1, 2, 3]) == 0
assert final_stone([1, 2, 3, 4]) == 0
assert final_stone([1, 2, 3, 4, 5]) == 1
assert final_stone([1, 1, 1, 1]) == 0
assert final_stone([1, 1, 1]) == 1
assert final_stone([1, 10, 1]) == 8
assert final_stone([1, 10, 1, 8]) == 0
assert final_stone([]) == 0
assert final_stone([1]) == 1
assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

print("The mission is done! Click 'Check Solution' to earn rewards!")
