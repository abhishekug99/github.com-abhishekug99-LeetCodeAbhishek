class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, ch):
            if (r, c) in visited:
                return True   

            visited.add((r, c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == ch:
                    if nr == pr and nc == pc:
                        continue
                    if dfs(nr, nc, r, c, ch):
                        return True

            return False

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False
    
    # def containsCycle(self, grid: List[List[str]]) -> bool:
    #     n = len(grid)
    #     m = len(grid[0])
    #     visited=set()

    #     def dfs(r,c,visited):
    #         start = (r,c)
    #         if r>=n or c>=m or r<0 or c<0 or (r,c) in visited:
    #             return False
    #         # if (r,c) in visited and (r,c)==start:
    #         #     return True
            
    #         if grid[r+1][c] and grid[r][c] == grid[r+1][c]: 
    #             dfs(r+1,c,visited)
    #         if grid[r][c+1] and grid[r][c] == grid[r][c+1]:
    #             dfs(r,c+1,visited)
    #         if grid[r-1][c] and grid[r][c] == grid[r-1][c]:
    #             dfs(r-1,c,visited)
    #         if grid[r][c-1] and grid[r][c] == grid[r][c-1]:
    #             dfs(r,c-1,visited)
            
    #         visted.add((r,c))

    #         if (r,c)==(0,0):
    #             return True
            
    #         return False
        

    #     res = None
    #     # for r in range(n):
    #     #     for c in range(m):
    #     #         res = dfs(r,c,visited)
        
    #     return dfs(0,0,visited)

    