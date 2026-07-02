class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        #BFS
        startHealth = health - grid[0][0]
        if startHealth<=0:
            return False
        
        best = [[-1]*m for _ in range(n)]
        best[0][0] = startHealth

        pq = [(-startHealth, 0, 0)]

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        while pq:
            negHealth,r,c = heapq.heappop(pq)
            curHealth = -negHealth

            if curHealth<best[r][c]:
                continue
            
            if r == n-1 and c == m-1:
                return True
            
            for dr,dc in dirs:
                nr = dr+r
                nc = dc+c

                if 0<=nr<n and 0<=nc<m:
                    newHealth = curHealth - grid[nr][nc]
                    if newHealth>0 and newHealth>best[nr][nc]:
                        best[nr][nc] = newHealth
                        heapq.heappush(pq, (-newHealth,nr,nc))
        
        return False
        
        # visited = set()
        
        # def dfs(r, c, h):
            
        #     if r < 0 or c < 0 or r >= n or c >= m:
        #         return False
        #     if (r, c) in visited:
        #         return False
        #     if grid[r][c] == 1:
        #         h -= 1
        #     if h <= 0:
        #         return False
        #     if r == n - 1 and c == m - 1:
        #         return True
            
            
        #     visited.add((r, c))
            
        #     if (dfs(r + 1, c, h) or
        #     dfs(r - 1, c, h) or
        #     dfs(r, c + 1, h) or
        #     dfs(r, c - 1, h)):
        #         return True

        #     visited.remove((r, c))
            
        #     return False
        
        # return dfs(0, 0, health)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna