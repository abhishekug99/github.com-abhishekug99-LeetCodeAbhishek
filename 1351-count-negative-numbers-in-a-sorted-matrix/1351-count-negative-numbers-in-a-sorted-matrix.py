class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        # linear time
        n,m= len(grid), len(grid[0])
        i,j = 0, m-1
        while i<n and j>=0:
            if grid[i][j]<0:
                res += n-i
                j-=1
            else:
                i+=1
        return res



        #correct abd submitted but possible in linear time
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])-1,-1,-1):
        #         if grid[i][j]<0:
        #             res+=1
        #         else:
        #             break
        # return res
