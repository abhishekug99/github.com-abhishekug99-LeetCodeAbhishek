class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        res = []
        n,m = len(grid), len(grid[0])
        visited = set()
        
        @lru_cache(maxsize=None)
        def dfs(r,c):
            prod = grid[r][c]
            if r==0 and c==0:
                return(prod,prod)
            vals = []
            if c>0:
                prevMax, preMin = dfs(r, c-1)
                vals += [prevMax*prod, preMin*prod]
            if r>0:
                prevMax, preMin = dfs(r-1, c)
                vals += [prevMax*prod, preMin*prod]

            return (max(vals),min(vals))

        maxP, minP = dfs(n-1,m-1)
        return maxP%MOD if maxP>=0 else -1


        #works well but not submitted
        # @lru_cache
        # def dfs(r, c, prod):
        #     if r >= n or c >= m:
        #         return float('-inf')
            
        #     prod *= grid[r][c]
            
        #     if r == n - 1 and c == m - 1:
        #         return prod if prod >= 0 else float('-inf')
            
        #     right = dfs(r, c + 1, prod)
        #     down = dfs(r + 1, c, prod)
            
        #     return max(right, down)
        # res = dfs(0, 0, 1)
        # return res % MOD if res != float('-inf') else -1
        
