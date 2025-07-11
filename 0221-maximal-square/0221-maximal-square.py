class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Saving more timme
        if not matrix or not matrix[0]:
            return 0
    
        ROW = len(matrix)
        COL = len(matrix[0])
        
        dp = []
        for _ in range(ROW + 1):
            dp.append([0] * (COL + 1))

        maxSqr = 0

        for r in range(1, ROW + 1):
            for c in range(1, COL + 1):
                if matrix[r - 1][c - 1] == '1':
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                    maxSqr = max(maxSqr, dp[r][c])
        
        return maxSqr ** 2

        #my logic -Accepted O(R*C)
        # dp = []
        # ROW = len(matrix)+1
        # COL = len(matrix[0])+1 #extra row and col for not goin out of bound

        # for i in range(len(matrix)+1):
        #     dp.append([0]*COL)
        
        # for r in range(ROW-1):
        #     for c in range(COL-1):
        #         if matrix[r][c] == '1':
        #             dp[r][c] = 1+min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) # main logic
                    
        #         elif matrix[r][c] == '0':
        #             dp[r][c] = 0

        # maxSqr = 0
        # for rows in dp:
        #     maxSqr = max(maxSqr, max(rows))
        
        # return maxSqr**2 