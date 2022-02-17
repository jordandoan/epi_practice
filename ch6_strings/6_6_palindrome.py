# Test whether a string is palindromic, ignoring all nonalphanumeric characters
def palindrome(s: str) -> bool:
    start = 0
    end = len(s)-1
    while True:
        # Ignore any non alpha chars
        while not s[start].isalnum():
            start += 1
        # Ignore any non alpha chars
        while not s[end].isalnum():
            end -= 1
        # Need to check if we crossed each other, which means we are done
        if start > end:
            return True
        # Every pairing of letters from the beg and end need to be matching, or else its not palindromic
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1

print(palindrome("Ray a Ray"))