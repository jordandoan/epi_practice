# Remove duplicates from an array and return the number of unique elements

# This method cant return array yet. have to modify A somehow
def brute(A: [int]) -> int:
    ans = set()
    for num in A:
        if num not in ans:
            ans.add(num)
    return len(ans)

# O(1) space, modify in place
def best(A: [int]) -> int:
    prev = 0
    # Left pointer and right pointer. Left pointer indicates where unique value will be
    for i in range(1, len(A)):
        # If there A[i] and A[prev] are equal, t
        # then we just skip,
        # therefore increasing the gap between prev and i
        if A[i] != A[prev]:
            # Since we know that the two elements are different, we want to switch the element
            # after prev with the value at i
            # We are not swapping unique values, but rather possibly swapping the next value
            # (which could be a dupe) after prev
            # This lets us swap in place for unique elements at the beginning.
            # If prev = 0 and i = 1, and the values are diff, then we just swap in place because prev = 1 now
            prev += 1
            A[prev] = A[i]
    # L is prev + 1 because of 0 indexing
    return prev + 1
print(best([2,2,3,5,7]))
print(best([2,3,5,7,11,11,11,13]))