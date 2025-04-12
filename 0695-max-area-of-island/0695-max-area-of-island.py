class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit= set()
        maxArea = 0

        def dfs(grid,visit,r,c):
            ROW,COL = len(grid), len(grid[0])
            if min(r,c)<0 or r ==ROW or c==COL or grid[r][c]==0 or (r,c) in visit:
                return 0

            area=1
            visit.add((r,c))
            area+=dfs(grid,visit,r+1,c)
            area+=dfs(grid,visit,r-1,c)
            area+=dfs(grid,visit,r,c+1)
            area+=dfs(grid,visit,r,c-1)
            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and(r,c) not in visit:
                    currArea = dfs(grid,visit,r,c)
                    maxArea = max(currArea,maxArea)
        return maxArea