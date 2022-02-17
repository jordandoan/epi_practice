# given an array, compute the next permutation in lexicon order
# 1 1 2 3 -> 1 1 3 2
# 3 2 1 1 is the last perm
# 2 2 4 1 3 -> 2 2 4 3 1
# 2 4 3 2 1 -> 3 1 2 2 4 ?
# 1 2 3 1 -> 1 3 1 2
# 1 3 1 2 -> 1 3 2 1
# 1 3 2 1 -> 2 1 1 3

# one idea:
# go in reverse order and find the first pair where i (end of array) < i + 1 (front of array) then swap
# look at 1 3 1 2, since we have 2 > 1, we just swap for 1 3 2 1
# but how does this work for 2 4 3 2 1 -> 3 1 2 2 4?
# based off line 11, we would have 4 2 3 2 1, which is not even close
# how do we know what value to swap out, maybe have to reiterate again FORWARD / towards the end of the array
# i know we have to swap the right value, then sort the rest of the array to get the next permutation

def next_perm(A):
    end = len(A)-1
    while end > 0:
        # if front element is less  than back element, complete the swap
        if A[end-1] < A[end]:
            # NEED FIND PROPER SORT METHOD
            next_min = float('inf')
            next_min_idx = 0
            for i in range(end, len(A)):
                # finding the NEXT MIN greater than the value we're swapping A[end-1]
                # in 2, 4 ,3,2,1 we need to find the 3 because the next lexicon order is 3 1 2 2 4
                if A[i] > A[end-1] and A[i] <= next_min:
                    next_min = min(next_min, A[i])
                    next_min_idx = i
            # we swap with next_min_idx
            A[end-1], A[next_min_idx] = A[next_min_idx], A[end-1]
            # sort the rest of the array because we are resetting the lexicon in a way
            # actually reverse just works because the subarray should be in decreasing order, we need incrasing order for minimum lexicon
            partial = reversed(A[end:])
            A[end:] = partial
            return A
        end -= 1
    # if elements are in decreasing order, return nothing because thats the end
    if end == 0:
        return []

# print(next_perm([3,2,1,1]))
# print(next_perm([1,3,1,2])) # 1 3 2 1
# print(next_perm([1,2,3,1])) # 1 3 1 2
# print(next_perm([2,4,3,2,1])) # 3 1 2 2 4
A = [1,5,5,5,3,1]
print(next_perm(A))