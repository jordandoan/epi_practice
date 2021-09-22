def advance(A: [int]) -> bool:
    max_pos = 0
    # interate through array, make sure the pos we are on is reachable from the start,
    # which is tracked by max_pos
    for pos, steps in enumerate(A):
        if max_pos >= pos:
            # find new max distance we can travel, which is the position of array + value in array
            max_pos = max(max_pos, pos + steps)
        else:
            return False
    return True
print(advance([3,3,1,0,2,0,1]))