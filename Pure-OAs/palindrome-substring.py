"""
A string S is called palindome if it reads same way if spelled backwards, for example: "nolemonnomelon", "ASANtaLivedAsAdeviLatNASA".

Any non-empty string has substrings that are palindromes. For example, in the string S="hellolle", there are many of such "subparlindromes":

1) ellolle

2) II, II-note that these are two distinct substrings that only happen to be equal

3) lol and Iloll

4) And, of course, each letter can be considered a palindrome - all 8 of them.

Write a function that, given a string S (that only consists of lowercase English letters), counts how many different ways are there to pick a palindrome substring from S.

Examples:

1. Input: hellolle

output: 13 (the above example)

2. Input: wowpurerocks

output: 14 (each letter + "wow" + "rer")
"""

def count_palindrome_substrings(s: str) -> int:
    n = len(s)
    count = 0

    # Expand around each index for odd-length palindromes.
    for center in range(n):
        left = right = center
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    # Expand around each adjacent pair for even-length palindromes.
    for center in range(n):
        left = center
        right = center + 1
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    return count

# Test the function with the provided examples:
if __name__ == '__main__':
    example1 = "hellolle"
    example2 = "wowpurerocks"
    print("Input:", example1, "Output:", count_palindrome_substrings(example1))  # Expected output: 13
    print("Input:", example2, "Output:", count_palindrome_substrings(example2))  # Expected output: 14
