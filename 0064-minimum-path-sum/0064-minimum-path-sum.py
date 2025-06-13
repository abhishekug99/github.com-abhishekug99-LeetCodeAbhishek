class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #dp O(m*n)
        ROW = len(grid)
        COL = len(grid[0])
        dp = [[float('inf')]*(COL+1) for i in range(ROW+1)]
        dp[ROW][COL-1] = 0
        # print(dp)
        for r in range(ROW-1,-1,-1):
            for c in range(COL-1,-1,-1):
                dp[r][c] = grid[r][c]+min(dp[r+1][c],dp[r][c+1])
                # print(dp)
        

        return dp[0][0]

        
        

        #dfs
        # ROW = len(grid)
        # COL = len(grid[0])
        # cache = {}
        # def dfs(r,c):
        #     if r >= ROW or c >= COL:
        #         return float('inf')
        #     if  r==ROW-1 and c ==COL-1:
        #         return grid[r][c]
        #     if (r,c) in cache:
        #         return cache[(r,c)]
            
        #     right = dfs(r,c+1)
        #     down = dfs(r+1,c)
        #     cache[(r,c)] = grid[r][c] + min(right,down)
        #     # print(cache)
        #     return cache[(r,c)]

        # return dfs(0,0)
         
    
