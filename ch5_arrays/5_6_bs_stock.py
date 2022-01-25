
# given a list of integers
# u can buy a stock and sell it at any time (after you buy it)
# find the maximum profit and return it
def stock(prices: [int]) -> int:
    current_min = float('inf')
    profit = 0
    # find the min as we go in chronological order
    # we always want the best lowest price for the best local max profit
    # if the max occurs after the low, then we will always get max profit
    # we just compare profits after every iteration to find the best possible profit
    for price in prices:
        current_min = min(price, current_min)
        profit = max(profit, price-current_min)
    return profit

# runtime O(n). Iteration
# space O(1). Only saving constants


#find length of longest subarray where all entries are equal
def equal_sub(nums: [int]) -> int:
    if not nums:
        return 0
    ans = 1
    current = 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            current += 1
        else:
            current = 1
        ans = max(ans,current)
    return ans
