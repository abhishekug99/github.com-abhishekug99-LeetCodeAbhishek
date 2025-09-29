class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for idx in range(3, n+1):
            for i in range(0, n-idx+1):
                j = i+idx-1
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i]*values[j]*values[k]
                    dp[i][j] = min(dp[i][j], cost)
        # print(dp)
        return dp[0][n-1]