class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i,j = 0,0
        # res =[]
        # while i<len(word1) or j<len(word2):
        #     if i<len(word1):
        #         res.append(word1[i])
        #         i+=1
        #     if j<len(word2):
        #         res.append(word2[j])
        #         j+=1
        # return ''.join(res)
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

         