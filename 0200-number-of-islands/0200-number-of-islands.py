class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        
        def dfs(grid,visit,r,c):
            ROW = len(grid)
            COl = len(grid[0])
            if min(r,c)<0 or r == ROW or c == COl or grid[r][c]=='0' or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(grid,visit,r+1,c)
            dfs(grid,visit,r-1,c)
            dfs(grid,visit,r,c+1)
            dfs(grid,visit,r,c-1)

        islandFound = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(grid,visit,r,c)
                    islandFound+=1
        
        return islandFound  