class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        seen = set()
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(words[i-1]):
                res.append(words[i])
        
        return words if not res else res
        