class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[-1] * (k + 1) for _ in range(m)]

        initcost = 1 if grid[0][0] in (1, 2) else 0
        initscore = grid[0][0]

        if initcost <= k:
            dp[0][initcost] = initscore

        for r in range(n):
            tmpdp = [[-1] * (k + 1) for _ in range(m)]

            for c in range(m):
                for cost in range(k + 1):
                    if dp[c][cost] == -1:
                        continue

                    if c + 1 < m:
                        nc = cost + (1 if grid[r][c + 1] in (1, 2) else 0)
                        if nc <= k:
                            dp[c + 1][nc] = max(
                                dp[c + 1][nc],
                                dp[c][cost] + grid[r][c + 1]
                            )

                    if r + 1 < n:
                        nc = cost + (1 if grid[r + 1][c] in (1, 2) else 0)
                        if nc <= k:
                            tmpdp[c][nc] = max(
                                tmpdp[c][nc],
                                dp[c][cost] + grid[r + 1][c]
                            )
            if r + 1 < n:
                dp = tmpdp
        ans = max(dp[m - 1])
        return ans if ans != -1 else -1

        # logically correct but not optimal
        # iniscore = [-1]
        # @lru_cache
        # def dfs(r,c,cost,score):
        #     cur=0
        #     if r<0 or c<0 or r>=n or c>=m:
        #         return
            
        #     if grid[r][c] == 1:
        #         cost+=1
        #         score +=1
        #     elif grid[r][c] == 2:
        #         cost+=1
        #         score +=2

        #     if cost>k:
        #        return

        #     if r==n-1 and c==m-1:
        #         iniscore[0] = max(iniscore[0], score)
        #         return
            
        #     # visited.add((r,c))
        #     dfs(r+1,c,cost,score)
        #     dfs(r,c+1,cost,score)
        #     # visited.remove((r,c))

        #     # return iniscore[0]

        # dfs(0,0,0,0)
        # return iniscore[0]


            

            
