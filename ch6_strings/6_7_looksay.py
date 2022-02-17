# Sequence starts with 1, then the next entry is reading off the previous entry: "one 1" => [1, 11]
# entry #2 is "two one" => [1, 11, 21]
# find the nth entry in the look say sequence
# algo, look for consecutive strings, then append [streak, char]
import string

# time complexity: n^2? Concatenating strings take O(n) time
# Was thinking about using arrays, but appending also takes O(n) time (due to resizing of array)
def look_say(n):
    ans = ["1"]*n
    for i in range(1,n):
        prev = ans[i-1]
        count = 1
        s = ""
        for j in range(len(prev)-1):
            if prev[j] != prev[j+1]:
                s += string.digits[count] + prev[j]
                count = 1
            else:
                count += 1
        s += string.digits[count] + prev[-1]
        ans[i] = s
    return ans[-1]

print(look_say(8))