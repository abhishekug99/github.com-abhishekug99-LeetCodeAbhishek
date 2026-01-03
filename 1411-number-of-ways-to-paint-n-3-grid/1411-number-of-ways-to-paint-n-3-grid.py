class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9+7
        pattern = []
        for r in range(3):
            for y in range(3):
                for g in range(3):
                    if r!=y and y!=g:
                        pattern.append((r,y,g))
        m = len(pattern)
        compatibility = [[] for _ in range(m)]
        # print(pattern)
        for i in range(m):
            for j in range(m):
                if all(pattern[i][k] != pattern[j][k] for k in range(3)):
                    compatibility[i].append(j)
                
        dp = [1]*m
        for _ in range(1,n):
            newDp = [0]*m
            for i in range(m):
                for j in compatibility[i]:
                    newDp[j] = (newDp[j]+dp[i])%MOD
            dp = newDp
        return sum(dp)%MOD