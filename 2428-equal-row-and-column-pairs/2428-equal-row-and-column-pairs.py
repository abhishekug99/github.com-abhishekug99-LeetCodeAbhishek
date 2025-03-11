class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rowColCnts = defaultdict(int)
        cnt = 0
        for row in grid:
            rowColCnts[tuple(row)] +=1

        for col in zip(*grid):
            cnt += rowColCnts[col]
        
        return cnt


        
        # j=0
        # grid2 = []
        # cnt = 0
        # n = len(grid)
        # for i in range(n):
        #     grid2In =[]
        #     for j in range(n):
        #        grid2In.append(grid[j][i])
        #     grid2.append(grid2In)
        # # print(grid2)
        
        # for row in grid:
        #     if row in grid2 or grid2 in row:
        #         cnt+=1
        #     else: continue
        # return cnt        

         
