class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Actual bottom to top dp O(m)
        prevRow = [0]*n
        for r in range(m-1,-1,-1):
            currRow = [0]*n
            currRow[n-1] = 1
            for c in range(n-2,-1,-1):
                currRow[c] = currRow[c+1]+prevRow[c]
            prevRow = currRow
        return prevRow[0]

        
        # top to bottom dp O(m*n)
        # cache = [[0]*n for _ in range(m)]
        # # print(cache)
        # def memoization(r,c,row,col):
        #     if r == row or c == col:
        #         return 0
        #     if cache[r][c]>0:
        #         return cache[r][c]
        #     if r == row-1 or c == col-1:
        #         return 1
        #     cache[r][c] = (memoization(r+1,c,row,col) + memoization(r,c+1,row,col))
        #     return cache[r][c]
    
        # return memoization(0, 0, m, n)
        