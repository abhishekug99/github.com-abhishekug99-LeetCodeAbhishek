class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #1ms using lru_cache for memoization with O(m*n)
        if obstacleGrid[-1][-1] == 1:
            return 0
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        @lru_cache
        def dfs(r,c):
            if r == ROW-1 and c==COL-1:
                return 1
            if min(r,c)<0 or r==ROW or c==COL or obstacleGrid[r][c] == 1:
                return 0
            cnt = 0
            cnt+=dfs(r+1,c)
            cnt+=dfs(r,c+1)
            return cnt

        return dfs(0,0)
        
        
        # my correct dfs+backtracking approach with time O(2^(r+c)) works well, TLE is there
        # ROW = len(obstacleGrid)
        # COL = len(obstacleGrid[0])
        # if obstacleGrid[-1][-1] == 1:
        #     return 0
        # visited = set()
        # def dfs(r,c,grid):
        #     if r == ROW-1 and c==COL-1:
        #         return 1
        #     if min(r,c)<0 or r==ROW or c==COL or (r,c) in visited or grid[r][c] == 1:
        #         return 0
        #     visited.add((r,c))
        #     cnt = 0
        #     cnt+=dfs(r+1,c,grid)
        #     cnt+=dfs(r,c+1,grid)
        #     visited.remove((r,c))
        #     return cnt

        # return dfs(0,0,obstacleGrid)
        