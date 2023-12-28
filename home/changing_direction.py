# speedy solution
# from itertools import pairwise
# def changing_direction(e: list) -> int:
#     return sum(x*y<0 for x,y in pairwise(x-y for x,y in pairwise(e) if x!=y))

# my solution
def changing_direction(elements: list[int]) -> int:
    count = 0
    up = False
    down = False
    cur_elem = elements[0]
    for elem in elements:
        if elem == cur_elem:
            cur_elem = elem
            continue
        elif elem > cur_elem:
            cur_elem = elem
            if up:
                continue
            elif down:
                count += 1
                up, down = True, False
                continue
            else:
                up, down = True, False
                continue
        elif elem < cur_elem:
            cur_elem = elem
            if down:
                continue
            if up:
                count += 1
                up, down = False, True
                continue
            else:
                up, down = False, True
                continue
    return count


# These "asserts" are used for self-checking
print(changing_direction([1, 2, 3, 4, 5]))
print(changing_direction([1, 2, 3, 2, 1]))
print(changing_direction([1, 2, 2, 1, 2, 2]))
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
