class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        
        def dfs(grid, visit, r):
            for c in range(len(grid)):
                if grid[r][c] == 1 and  c not in visit:
                    visit.add(c)
                    dfs(grid, visit, c)

        res = 0
        for r in range(len(isConnected)):
            if r not in visit:
                visit.add(r)
                dfs(isConnected,visit,r)
                res+=1
        return res

        # visit = set()
        # def dfs(grid,visit,r,c):
        #     ROW, COL = len(grid), len(grid[0])
        #     'logic'
        #     if (r,c) in visit or min(r,c)<0 or r == ROW or c == COL or grid[r][c] == 0:
        #         return 0
        #     if r!=c:
        #         if grid[r][c] == 1 and (r,c) not in visit: 
        #             visit.add((r,c))        
        #             return 1

            
        #     cnt =0

        #     cnt+=dfs(grid,visit,r+1,c)
        #     cnt+=dfs(grid,visit,r-1,c)
        #     cnt+=dfs(grid,visit,r,c+1)
        #     cnt+=dfs(grid,visit,r,c-1)
        #     # visit.remove((r,c))

        #     return cnt
        # res = dfs(isConnected,visit,0,0)
        # return res if res>0 else len(isConnected)
        