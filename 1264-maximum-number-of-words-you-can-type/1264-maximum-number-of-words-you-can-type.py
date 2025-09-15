class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        txt = text.split(' ')
        res = 0
        for word in txt:
            if all(b not in word for b in brokenLetters):  # check all broken letters
                res += 1
        return res
