class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m-k+1):
            row=[]
            for j in range(n-k+1):
                vals=[]
                for r in range(i, i+k):
                    for c in range(j, j+k):
                        vals.append(grid[r][c])
                vals = sorted(set(vals))
                if len(vals)==1:
                    row.append(0)
                else:
                    minDiff = min(vals[x+1]-vals[x] for x in range(len(vals)-1))
                    row.append(minDiff)
            res.append(row)
        return res