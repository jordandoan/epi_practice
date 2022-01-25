arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]

def delete_duplicate(A):
    i = 0
    while i < len(A)-1:
        if A[i] == A[i+1]:
            A.pop(i)
        else:
            i += 1
    return len(A)

def delete_duplicate_opt(A):
    if not A:
        return 0
    current = 1
    for i in range(1, len(A)):
        if A[current - 1] != A[i]:
            A[current] = A[i]
            current += 1
        print(arr)
    return current

# print(delete_duplicate_opt(arr))
# print(arr)


def isValid(s):
    s = []

    pairs = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    for ch in s:
        print(ch)
        if ch not in pairs:
            s.append(ch)
        else:
            if not len(s):
                return False
            if pairs.get(ch) == s[-1]:
                s.pop()
            else:
                return False
            # if len(s) and pairs[ch] == s[-1]:
            #     s.pop()
            # else:
            #     return False
    return not s

print(isValid('(]'))