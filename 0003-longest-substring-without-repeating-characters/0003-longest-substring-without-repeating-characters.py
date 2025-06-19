class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCnt = 0
        visited = set()
        j=0
        for i in range(len(s)):
            if s[i] in s[j:i]:
                j= j+s[j:i].index(s[i])+1
            maxCnt = max(maxCnt, i-j+1)
        
        return maxCnt
