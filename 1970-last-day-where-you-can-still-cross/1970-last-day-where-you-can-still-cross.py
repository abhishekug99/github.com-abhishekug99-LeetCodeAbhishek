class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def canWalk(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r,c = cells[i]
                grid[r-1][c-1]=1
            q=deque()
            visited = [[False]*col for _ in range(row)]
            for c in range(col):
                if grid[0][c]==0:
                    q.append((0,c))
                    visited[0][c]=True
            while q:
                r,c = q.popleft()
                if r==row-1:
                    return True
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<row and 0<=nc<col and not visited[nr][nc] and grid[nr][nc]==0:
                        visited[nr][nc]=True
                        q.append((nr,nc))
            return False

        low, high = 0, len(cells)
        while low<high:
            mid = (low+high+1)//2
            if canWalk(mid):
                low = mid
            else:
                high=mid-1
        return low




        # print(grid)
        #works great but TLE
        # grid = [[0]*col for _ in range(row)]
        # def dfsCanWalk(grid, visited, r,c):
        #     if r<0 or c<0 or r>=row or c>=col:
        #         return  False
            
        #     if grid[r][c] == 1 or (r, c) in visited:
        #         return False

        #     if r==row-1:
        #         return True
    
        #     visited.add((r,c))
        #     return(dfsCanWalk(grid, visited, r+1,c) or
        #         dfsCanWalk(grid, visited, r-1,c) or 
        #         dfsCanWalk(grid, visited, r,c+1) or
        #         dfsCanWalk(grid, visited, r,c-1))
                        
        # res = 0         
        # for day in range(1, len(cells)+1):
        #     r, c = cells[day-1]
        #     grid[r-1][c-1] = 1
        #     canWalk=False
        #     visited = set()
        #     for C in range(col):
        #         if grid[0][C]==0 and dfsCanWalk(grid, visited, 0,C):
        #             canWalk = True
        #             break
        #     if canWalk:
        #         res = day
        #     else:
        #         return day-1

        # return res
                    


            

