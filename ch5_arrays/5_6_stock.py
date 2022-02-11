def stock(A: [int]) -> int:
    low_so_far = A[0]
    profit = 0
    for i in range(1, len(A)):
        if A[i] < low_so_far:
            low_so_far = A[i]
        profit = max(profit, A[i] - low_so_far)
    return profit

print(stock([310, 315,275,295,260,270,290,230,255,250]))