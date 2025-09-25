import heapq
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]*(len(triangle)+1)
        for r in triangle[::-1]:
            for i,n in enumerate(r):
                dp[i] = min(dp[i], dp[i+1])+n
        
        return dp[0]

        # if len(triangle) == 1:
        #     return triangle[0][0]
        
        # for i in range(len(triangle)-2,-1,-1):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1] )
        # return triangle[0][0]

        