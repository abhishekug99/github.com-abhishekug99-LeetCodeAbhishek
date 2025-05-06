class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # O(m*n)
        if text1 == text2:
            return len(text1)

        m, n = len(text1), len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1        
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        # print(dp)
        return dp[m][n]

        # print(dp)

        # if text1 == text2:
        #     return len(text1)
        # dp = ['']*len(text1)
        # j = 0
        # i = 0
        # for char in text2:
        #     if char in text1 and j<len(text1) and char not in text1[:i]:
        #         if i<len(text1) and char not in text1[:i] and char not in dp:
        #             dp[j] = char
        #             j+=1
        #     i+=1
        # print(dp)
        # return len(''.join(dp))
        
        