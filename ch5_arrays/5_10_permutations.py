# given an array A and a perm P where P has entries 0 to n (n is length of A), return the permutation of A in space.
# A = [a b c d] P = [2 0 1 3] should return [b c a d]
# iterating as i:
# P[i] = j,
# A[i] should be at position j
# ex reads as:
# the first value should be at pos 2
# the second val should be at pos 0
# the third pos should be at pos 1
# etc

# in this algo
# we are filling out where the i-th value goes
# aka we are not filling out the array from 0 to n-1
def ex_space(A, P):
    ans = [0]*len(A)
    for i in range(len(A)):
        j = P[i]
        ans[j] = A[i]
    return ans

A = ['a','b','c','d']
P = [0,3,2,1]
print(ex_space(A,P))

# we can swap values in the same array,
# the permutation only denotes what position the i-th value should be at, so when we swap in the array,
# we can swap the values in the permutation, because they are linked in a sense
# for example if we had [abcd] and [2,0,1,3]
# it tells us that that the first value should be at pos 2
# so we get cbad
# we have to swap the perm values because we still havent swapped the c yet so we get
# [1,0,2,3]
# this tells us that c should be at pos 1, so we swap
# [0,1,2,3]
def swap(A,P):
    for i in range(len(A)):
        while i != P[i]:
            ## store value at pos denoted by P[i] aka J
            ## replace value at pos j with A[i]
            ## replace value at A[i] with stored value
            # tempA = A[P[i]]
            # A[P[i]] = A[i]
            # A[i] = tempA

            ## store pos value P[i] aka J
            ## swap value stored in P[i] with value at pos J
            ## replace value at pos J with value J (i think?)
            # tempP = P[i]
            # P[i] = P[tempP]
            # P[tempP] = tempP
            # Same as above but shorter
            A[P[i]], A[i] = A[i], A[P[i]]
            P[P[i]], P[i] = P[i], P[P[i]]
    return A
print(swap(A, P))