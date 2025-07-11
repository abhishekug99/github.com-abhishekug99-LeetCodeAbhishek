class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        ROW = len(matrix)+1
        COL = len(matrix[0])+1

        for i in range(len(matrix)+1):
            dp.append([0]*COL)
        
        for r in range(ROW-1):
            for c in range(COL-1):
                if matrix[r][c] == '1':
                    dp[r][c] = 1+min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    
                elif matrix[r][c] == '0':
                    dp[r][c] = 0

        maxSqr = 0
        for rows in dp:
            maxSqr = max(maxSqr, max(rows))
        
        return maxSqr**2 