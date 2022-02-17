def pascal(n):
    ans = []
    for i in range(1,n+1):
        if i <= 2:
            ans.append([1]*i)
        else:
            current = [1]*(i)
            for j in range(1,i-1):
                current[j] = ans[-1][j-1] + ans[-1][j]
            ans.append(current)
    return ans

print(pascal(5))