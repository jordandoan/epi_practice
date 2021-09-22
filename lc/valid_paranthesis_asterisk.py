def checkValidString(s):
    count = 0
    for ch in s:
        if ch == "(":
            count += 1
        elif ch == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0
print(checkValidString("()") == True)