class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        INF = float('-inf')
        
        # dp[r][c][k]
        dp = [[[INF]*3 for _ in range(n)] for _ in range(m)]
        
        # base: last cell
        for k in range(3):
            if coins[m-1][n-1] < 0 and k > 0:
                dp[m-1][n-1][k] = 0
            else:
                dp[m-1][n-1][k] = coins[m-1][n-1]
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c == n-1:
                    continue
                    
                for k in range(3):
                    best = INF
                    for nr, nc in [(r+1, c), (r, c+1)]:
                        if nr < m and nc < n:
                            val = coins[r][c]
                            
                            if val >= 0:
                                best = max(best, val + dp[nr][nc][k])
                            else:
                                best = max(best, val + dp[nr][nc][k])
                                
                                if k > 0:
                                    best = max(best, dp[nr][nc][k-1])
                    
                    dp[r][c][k] = best
        
        return dp[0][0][2]
        
        # m, n = len(coins), len(coins[0])
        # @lru_cache(None)
        # def dfs(r, c, k):
        #     if r >= m or c >= n:
        #         return float('-inf')

        #     val = coins[r][c]
        #     if r == m - 1 and c == n - 1:
        #         if val < 0 and k > 0:
        #             return 0
        #         return val

        #     if val >= 0:
        #         return val + max(dfs(r+1, c, k), dfs(r, c+1, k))

        #     take = val + max(dfs(r+1, c, k), dfs(r, c+1, k))

        #     skip = float('-inf')
        #     if k > 0:
        #         skip = max(dfs(r+1, c, k-1), dfs(r, c+1, k-1))

        #     return max(take, skip)

        # return dfs(0, 0, 2)