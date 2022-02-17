def column(id: str) -> int:
    ans = 0

    for i, ch in enumerate(reversed(id)):
        num_val = ord(ch)-64
        ans += (num_val * (pow(26,i)))
    return ans
print(column('AA'))

def num_to_column(n: int) -> str:
    s = ""
    while n > 0:
        val = (n-1) % 26 + 1
        ch = chr(val+64)
        n = (n-1) // 26
        s += ch
    return s[::-1]

print(num_to_column(53))