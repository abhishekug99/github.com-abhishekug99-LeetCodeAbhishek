class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [[False]*(len(s2)+1)for i in range(len(s1)+1)] #extra layer to check out of bounds
        dp[len(s1)][len(s2)]=True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]
        # works well with dfs O(m*n)
        # dp = {}
        # def dfs(m,n):
        #     if m==len(s1) and n ==len(s2):
        #         return True
        #     if (m,n) in dp:
        #         return dp[(m,n)]
        #     if m<len(s1) and s1[m] == s3[m+n] and dfs(m+1,n):
        #         return True
        #     if n<len(s2) and s2[n] == s3[m+n] and dfs(m,n+1):
        #         return True
        #     dp[(m,n)]=False
        #     return False
        # return dfs(0,0)
        