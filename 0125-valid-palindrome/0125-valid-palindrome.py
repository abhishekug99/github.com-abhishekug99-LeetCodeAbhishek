class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        s = re.sub(r'[, ;:.]', "", s)
        print(s)
        if s==s[::-1]:
            return True
        return False