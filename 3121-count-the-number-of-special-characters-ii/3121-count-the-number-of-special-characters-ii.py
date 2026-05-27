class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lastLower = {}
        firstUpper = {}

        for i, ch in enumerate(word):

            if ch.islower():
                lastLower[ch] = i
            else:
                c = ch.lower()
                if c not in firstUpper:
                    firstUpper[c] = i

        res = 0
        for ch in lastLower:
            if ch in firstUpper and lastLower[ch] < firstUpper[ch]:
                res += 1
        return res
