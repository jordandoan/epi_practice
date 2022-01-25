from collections import defaultdict

# Calculates all possible combinations of triplets
# Keeps a memo of values with its complements that equals 0 to ensure no duplicates
# Runtime O n^3 - triple for loop
# Space O n - memo can have n entries
def brute(nums: [int]) -> [[int]]:
    L = len(nums)
    ans = []
    memo = defaultdict(set)
    for i in range(L - 2):
        for j in range(i + 1, L - 1):
            for k in range(j + 1, L):
                if nums[i] + nums[j] + nums[k] == 0:
                    pos = [nums[i], nums[j], nums[k]]
                    pos.sort()
                    complement = (pos[1],pos[2])
                    if complement not in memo[pos[0]]:
                        memo[pos[0]].add(complement)
                        ans.append(pos)
    return ans

print(brute([-1,0,1,2,-1,-4]))

def optimal(nums: [int]) -> [[int]]:
    nums.sort()
    i, j, k = 0, 1, len(nums)-1
