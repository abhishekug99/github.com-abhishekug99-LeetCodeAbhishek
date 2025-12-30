class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n<3 or m<3:
            return 0
        
        def isMagic(r,c,grid):
           vals = set()
           for i in range(r,r+3):
            for j in range(c,c+3):
                if grid[i][j]<1 or grid[i][j]>9:
                    return False
                vals.add(grid[i][j])
           if len(vals)!=9:
            return False
           goal = grid[r][c] + grid[r][c+1] + grid[r][c+2]

           for i in range(3):
            if sum(grid[r+i][c:c+3]) != goal:
                return False
            if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != goal:
                return False
           if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != goal:
            return False
           if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != goal:
            return False

           return True

        res =0
        for r in  range(n-2):
            for c in range(m-2):
                if isMagic(r,c,grid):
                    res+=1
                else:
                    continue
        return res