class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        res=0
        for i in range(n):
            for j in range(m):
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i-1][j-1]
                    
                if grid[i][j] <= k:
                    res += 1

        return res
        
        # res=[0]
        # def dfs(r, c, curr):
        #     if r >= n or c >= m:
        #         return
            
        #     curr += grid[r][c]
            
        #     if curr <= k:
        #         res[0] += 1
        #     else:
        #         return   
            
        #     dfs(r + 1, c, curr)
        #     dfs(r, c + 1, curr)
        # dfs(0,0,0)
        # return res[0]
            

            