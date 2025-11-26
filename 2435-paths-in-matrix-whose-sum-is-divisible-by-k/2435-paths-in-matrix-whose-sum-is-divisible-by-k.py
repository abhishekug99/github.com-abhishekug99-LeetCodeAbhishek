class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        #Optimised dfs O(m*n*k)
        MOD = 10**9 + 7
        ROW = len(grid)
        COL = len(grid[0])
        cache = [[[-1]*k for _ in range(COL)] for _ in range(ROW)]
        
        def dfs(r,c, remain):
            if (r == ROW-1 and c == COL-1):
                remain = (remain + grid[r][c])%k
                return 0 if remain else 1
            if r==ROW or c==COL:
                return 0
            if cache[r][c][remain]>-1:
                return cache[r][c][remain]
            cache[r][c][remain] = (
                dfs(r+1, c, (remain + grid[r][c]) % k) % MOD +
                dfs(r, c+1, (remain+grid[r][c])%k) % MOD
            ) % MOD
            return cache[r][c][remain]
        
        return dfs(0,0,0)

        # correct approach O(2^(m+n))
        # MOD = 10**9 + 7
        # visited = set()
        # ROW = len(grid)
        # COL = len(grid[0])
        # cnt = 0
        # @lru_cache
        # def dfs(r,c, sumrc):
        #     if r<0 or r>=ROW or c<0 or c>=COL:
        #         return 0
            
        #     sumrc += grid[r][c]            
            
        #     if (r == ROW-1 and c == COL-1):
        #         return 1 if sumrc%k==0 else 0
            
        #     cnt=0
        #     cnt += dfs(r,c+1, sumrc)
        #     cnt += dfs(r+1,c, sumrc)
                        
        #     return cnt
        # res = dfs(0,0,0)
        # return res % MOD
        
        # correct approach O(2^(m+n))
        # def dfs(r,c,visited, sumrc):
        #     if r<0 or r>=ROW or c<0 or c>=COL or (r,c) in visited:
        #         return 0
            
        #     sumrc += grid[r][c]            
        #     visited.add((r,c))
            
        #     if (r == ROW-1 and c == COL-1):
        #         visited.remove((r,c))
        #         return 1 if sumrc%k==0 else 0
            
        #     cnt=0
        #     cnt += dfs(r,c+1,visited, sumrc)
        #     cnt += dfs(r+1,c,visited, sumrc)
            
        #     visited.remove((r,c))
            
        #     return cnt
        # res = dfs(0,0,visited,0)
        # return res % MOD
        

            
