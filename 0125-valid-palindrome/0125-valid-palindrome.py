class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = ''.join(c for c in s if c.isalnum()).lower()
        print(s)
        if s==s[::-1]:
            return True
        return False