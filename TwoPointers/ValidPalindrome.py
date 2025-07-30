def ValidPalindrome(string: str) -> bool:
    l, r = 0, len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

str = "abcdefgfedcba"
result = ValidPalindrome(str)
print(result)