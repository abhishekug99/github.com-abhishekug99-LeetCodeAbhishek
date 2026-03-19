class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        px = [[0]*m for _ in range(n)]
        py = [[0]*m for _ in range(n)]

        res = 0
        for i in  range(n):
            for j in range(m):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0

                px[i][j] = x
                py[i][j] = y

                if i>0:
                    px[i][j] += px[i-1][j]
                    py[i][j] += py[i-1][j]
                if j>0:
                    px[i][j] += px[i][j-1]
                    py[i][j] += py[i][j-1]
                if i > 0 and j > 0:
                    px[i][j] -= px[i-1][j-1]
                    py[i][j] -= py[i-1][j-1]
                if px[i][j] == py[i][j] and px[i][j] > 0:
                    res += 1

        return res
    
        # res = 0
        # xs = 0
        # ys = 0

        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 'X':
        #             xs += 1
        #         elif grid[i][j] == 'Y':
        #             ys += 1

        #         if xs == ys and xs > 0:
        #             res += 1

        # return res