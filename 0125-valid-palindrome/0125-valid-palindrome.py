class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = ''.join(c for c in s if c.isalnum()).lower()
        # s = s.lower
        r = len(s)
        print(r)
        i = 0
        j = len(s)-1
        mid  =  j//2
        while i<j:
            if s[i] != s[j]:
                return False
            elif s[i] != s[j]:
                continue
            i+=1
            j-=1
        return True
        
        