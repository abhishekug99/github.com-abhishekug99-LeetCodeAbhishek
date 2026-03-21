class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        def flipg(r,c,r1,c1):
            a = grid[r][c]
            grid[r][c] = grid[r1][c1]
            grid[r1][c1] = a


        for i in range(k // 2):
            for j in range(k):
                flipg(x + i, y + j, x + k - 1 - i, y + j)

        return grid
            
