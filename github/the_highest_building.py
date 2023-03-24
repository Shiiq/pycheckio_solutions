# The main architect of the city wants to build a new highest building.
# You have to help him find the current highest building in the city.
# The main architect of the city wants to build a new highest building.
# You have to help him find the current highest building in the city.
# Input: Heights of the buildings as a 2D-list.
# Building height is defined as a column in a list.
# Output: The number of the highest building and height of it as a list of integers
# (Important: in this task the building numbers starts from "1", not from "0").
from functools import wraps
from time import perf_counter
from random import randint

def get_sizeof_arr(size):
     arr = [[randint(0, 1) for _ in range(size)] for _ in range(size)]
     return arr


def exec_time(f):
    @wraps(f)
    def wrapper(array):
        start = perf_counter()
        res = f(array)
        total_time = perf_counter() - start
        print(f.__name__, res, "total time is ", total_time)
        return res
    return wrapper


@exec_time
def highest_building(buildings: list[list[int]]) -> list[int]:
    length = len(buildings[0])
    results = [
        [addr + 1, sum([floor[addr] for floor in buildings])] for addr in range(length)
    ]
    building = max(results, key=lambda x: x[1])
    return building


#  fastest version
@exec_time
def highest_building_2(buildings: list[list[int]]) -> list[int]:
    results = list(map(sum, zip(*buildings)))
    max_height = max(results)
    building = [results.index(max_height) + 1, max_height]
    return building


test_arr = get_sizeof_arr(1000)
highest_building(test_arr)
highest_building_2(test_arr)


assert highest_building([[0, 0, 1, 0],
                         [1, 0, 1, 0],
                         [1, 1, 1, 0],
                         [1, 1, 1, 1]]) == [3, 4]
assert highest_building([[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 1]]) == [4, 1]
print("The mission is done! Click 'Check Solution' to earn rewards!")