# in a string with words separated by whitespace, reverse the order of words
# alice likes bob => bob likes alice
# extra space approach: save words in an array using split, then reverse array and join words O(n) time
def reverse_words(s: str) -> str:
    words = s.split()
    return " ".join(words[::-1])

# in place approach
def reverse_in_place(s: str) -> str:
    s = list(s)
    start, end = 0, len(s)-1
    # reverses characrtesr within a range
    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
    reverse_range(s, 0, len(s)-1)
    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != " ":
            finish += 1
        if finish == len(s):
            return "".join(s)
        reverse_range(s, start, finish-1)
        # s[finish] is always " ", so we move to next work initializing at finish + 1
        start = finish + 1

print(reverse_words("bob likes alice"))
print(reverse_in_place("bob likes alice"))