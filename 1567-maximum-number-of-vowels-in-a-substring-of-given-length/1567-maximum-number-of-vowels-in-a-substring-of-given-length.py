class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        maxVowels = 0
        currCnt = 0
        r = k-1
        
        for i in range(k):
            if s[i] in vowels:
                currCnt += 1
        maxVowels = currCnt
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                currCnt += 1
            if s[i - k] in vowels:
                currCnt -= 1
            maxVowels = max(maxVowels, currCnt)
        return maxVowels
            

