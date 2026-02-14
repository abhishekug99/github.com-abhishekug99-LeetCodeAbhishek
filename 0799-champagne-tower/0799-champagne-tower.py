class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # query_row = query_row+1
        # totalGlasses = (query_row*(query_row+1))/2
        # if poured==0:
        #     return 0
        # if poured>totalGlasses:
        #     return 1.00
        
        # ratio = totalGlasses/poured
        # print(ratio)
        # if ratio<=0:
        #     return 0
        # else:
        #     res = ((str(ratio)).split('.'))[1]
        #     return float("0"+"."+res)

        dp = [[0.0]*(r+1) for r in range(query_row+1)]
        dp[0][0] = poured
        for r in range(query_row):
            for c in range(len(dp[r])):
                if dp[r][c]>1:
                    overflow = (dp[r][c]-1)/2
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow
                    dp[r][c] = 1
        print(dp)
        return min(1, dp[query_row][query_glass])