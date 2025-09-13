class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a','e','i','o','u']
        letters = {}
        vow = {}
        for i in range(len(s)):
            if s[i] in vowels:
                if s[i] not in vow:
                    vow[s[i]] = 1
                else:
                    vow[s[i]] += 1
            else:
                if s[i] not in letters:
                    letters[s[i]] = 1
                else:
                    letters[s[i]] += 1
        if not vow:
            return max(letters.values())
        elif not letters:
            return max(vow.values())
        else:
            return max(letters.values()) + max(vow.values())
    
