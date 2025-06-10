class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict = set(wordDict)
        # print(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[len(s)]

        
        # for char in s: 
        #     dp[j] += char
        #     if dp[j] in wordDict:
        #         j+=1
        # print(dp)
        # for word in dp:
        #     if word not in wordDict and word != '':
        #         return False
        # return True
                


