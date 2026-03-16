class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        res = set()

        for r in range(n):
            for c in range(m):
                # radius 0 rhombus
                res.add(grid[r][c])

                k = 1
                while r - k >= 0 and r + k < n and c - k >= 0 and c + k < m:
                    total = 0
                    # top right
                    i, j = r - k, c
                    while (i, j) != (r, c + k):
                        total += grid[i][j]
                        i += 1
                        j += 1
                    # right bottom
                    while (i, j) != (r + k, c):
                        total += grid[i][j]
                        i += 1
                        j -= 1
                    # bottom left
                    while (i, j) != (r, c - k):
                        total += grid[i][j]
                        i -= 1
                        j -= 1
                    # left top
                    while (i, j) != (r - k, c):
                        total += grid[i][j]
                        i -= 1
                        j += 1

                    res.add(total)
                    k += 1

        return sorted(res, reverse=True)[:3]
        
        
        # n = len(grid)
        # m = len(grid[0])
        # res = []
        # rhom =set()
        # def dfs(grid,r,c,sumR, rhom: set()):
        #     if r<0 or c<0 or r>=n or c>=m:
        #         return
        #     if r == 0 or r==n-1 or c==0 or c==m-1:
        #         sumR+=grid[r][c]  
        #     if (r,c) in rhom:
        #         return sumR
        #     rhom.add((r,c))
        #     dfs(grid, r+1, c+1, sumR, rhom)
        #     dfs(grid,r-1,c-1,sumR, rhom)
        #     dfs(grid,r+1,c-1,sumR, rhom)
        #     dfs(grid,r-1,c+1,sumR, rhom)
        #     rhom.add((r,c))
        
        # for r in range(n):
        #     for c in range(m):
        #         rSum=dfs(grid,r,c,grid[r][c], rhom)
        #         res.append(rSum)
        # return res