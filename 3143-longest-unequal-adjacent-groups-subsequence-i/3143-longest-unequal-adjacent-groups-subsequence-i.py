class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        if len(words) == 1:
            return words
        for i in range(1,len(words)):
            res.append(words[i])
            if groups[i-1]==groups[i]:
                res.pop()
        
        return res

        