class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2


        def dfs(r,c,dr,dc):
            nr, nc = r+dr, c+dc
            if not(0 <= nr < m and 0 <= nc < n):
                return
            if grid[nr][nc] in (1, 2):
                return
            if grid[nr][nc] == 3:
                dfs(nr,nc, dr,dc)
                return
            grid[nr][nc] =3
            dfs(nr,nc, dr,dc)
            
        for r, c in guards:
            for dr, dc in dirs:
                dfs(r, c, dr, dc)

        res = sum(grid[r][c]==0 for r in range(m) for c in range(n))
        return res
                    
                