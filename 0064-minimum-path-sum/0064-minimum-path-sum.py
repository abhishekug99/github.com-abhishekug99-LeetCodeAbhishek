class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        cache = {}
        def dfs(r,c):
            if r >= ROW or c >= COL:
                return float('inf')
            if  r==ROW-1 and c ==COL-1:
                return grid[r][c]
            if (r,c) in cache:
                return cache[(r,c)]
            
            right = dfs(r,c+1)
            down = dfs(r+1,c)
            cache[(r,c)] = grid[r][c] + min(right,down)
            print(cache)
            return cache[(r,c)]

        return dfs(0,0)
         
    
