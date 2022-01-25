def primes(n):
    # ans_set = set([i for i in range(1, n)])
    # for i in range(2, n+1):
    #     if i in ans_set:
    #         mult = 2
    #         while i * mult < n:
    #             ans_set.discard(i * mult)
    #             mult += 1
    # return ans_set
    arr = [True for i in range(n)]
    arr[0] = False
    ans = []
    for num in range(1, n+1):
        if arr[num-1]:
            ans.append(num)
            mult = 2
            while num * mult < n+1:
                arr[num*mult-1] = False
                mult += 1
    return ans
print(primes(1))
