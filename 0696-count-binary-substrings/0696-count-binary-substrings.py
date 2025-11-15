class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        res = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curr+=1
            else:
                res += min(prev, curr)
                prev = curr
                curr = 1
        res+= min(prev, curr)
        return res

# 00 111 00 11
#  2   3  2  2
# min(2,3) + min(3,2) + min(2,2)