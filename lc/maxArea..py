def maxArea(height: [int]) -> int:
    return brute(height)
def brute(height: [int]) -> int:
    ans = 0
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            ans = max(ans, (j-i)*min(height[i],height[j]))
    return ans