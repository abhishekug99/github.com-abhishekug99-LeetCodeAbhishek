class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        connectionMap={
        1: [(0,1),(0,-1)],
        2: [(1,0),(-1,0)],
        3: [(0,-1),(1,0)],
        4: [(0,1),(1,0)],
        5: [(0,-1),(-1,0)],
        6: [(0,1),(-1,0)],
        }
        donePaths = set()
        
        def canComeBack(nr,nc,r,c):
            for dr,dc in connectionMap[grid[nr][nc]]:
                if nr+dr==r and nc+dc==c:
                    return True
            return False

        def dfs(r,c):
            if (r,c) in donePaths:
                return False

            donePaths.add((r,c))

            if r == n-1 and c == m-1:
                return True
            
            for dr,dc in connectionMap[grid[r][c]]:
                nr,nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < m:
                    if canComeBack(nr,nc,r,c):
                        if dfs(nr,nc):
                            return True
            
            return False  
        
        return dfs(0,0)

