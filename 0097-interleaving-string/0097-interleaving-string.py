class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        dp = {}
        def dfs(m,n):
            if m==len(s1) and n ==len(s2):
                return True
            if (m,n) in dp:
                return dp[(m,n)]
            if m<len(s1) and s1[m] == s3[m+n] and dfs(m+1,n):
                return True
            if n<len(s2) and s2[n] == s3[m+n] and dfs(m,n+1):
                return True
            dp[(m,n)]=False
            return False
        return dfs(0,0)
        