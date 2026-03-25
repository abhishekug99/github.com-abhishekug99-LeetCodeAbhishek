class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        horizontal = [sum(row) for row in grid]
        total = sum(horizontal)
        
        prefix = 0
        for i in range(n - 1): 
            prefix += horizontal[i]
            if prefix == total - prefix:
                return True
        
        vertical = [0] * m
        for j in range(m):
            for i in range(n):
                vertical[j] += grid[i][j]
        
        total = sum(vertical)
        prefix = 0
        for j in range(m - 1):
            prefix += vertical[j]
            if prefix == total - prefix:
                return True
        
        return False
        # Time consuming but correct
        # horizontal=[]
        # n,m =len(grid), len(grid[0])
        # hor=0
        # vertical=[]
        # for i in range(n):
        #     horizontal.append(sum(grid[i]))

        # for i in range(n):
        #     if sum(horizontal[:i+1])==sum(horizontal[i+1:]):
        #         return True
        
        # for i in range(m):
        #     curr=0
        #     for j in range(n):
        #         curr+=grid[j][i]
        #     vertical.append(curr)
        
        # for i in range(m):
        #     if sum(vertical[:i+1])==sum(vertical[i+1:]):
        #         return True

        # return False