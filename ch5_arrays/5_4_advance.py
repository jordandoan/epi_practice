def advance(A: [int]) -> bool:
    a = 0
    while a < len(A)-1:
        steps = A[a]
        max_so_far = steps
        for i in range(steps):
            if max_so_far < steps + A[a+i+1]:
                max_so_far = steps + A[a+i+1]
                new_A = a + i
            max_so_far = max(max_so_far, steps + A[a + i + 1])
        if max_so_far == steps:
            return False
        else:
            a = new_A
    return True
print(advance([3,3,1,0,2,0,1]))