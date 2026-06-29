class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for c in patterns:
            if len(c)<=len(word) and (c==word or c in word):
                res+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna