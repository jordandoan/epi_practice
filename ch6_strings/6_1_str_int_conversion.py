import string

# Convert from str to int without converting types directly (using int or str)

def str_int(s: str) -> int:
    if not s:
        return 0
    ans = 0
    negative = False
    # checks for leading '-'
    if s[0] == "-":
         negative = True
    for c in  s[0:]:
        # this covers leading '+', so can start from 0 instead of 1
        if c.isdigit():
            # string.digits gives us '01234567890' while .index gives us the int value of c
            ans = ans * 10 + string.digits.index(c)
    # multiply by -1
    if negative:
        ans *= -1
    return ans

print(str_int('-12239393'))

# Convert from int to str without converting types directly
def int_str(n: int) -> str:
    negative = False
    if n < 0:
        negative = True
        # Need to make n positive because -1 // 10 = -1, not 0
        n *= -1
    ans = []
    while n != 0:
        # Take the rightmost digit and append to array
        ans.append(string.digits[n % 10])
        # Cut off right most digit
        n = n // 10
    if negative:
        ans.append('-')
    ans.reverse()
    ans = "".join(ans)
    return ans
print(type(int_str(1234)) == str)