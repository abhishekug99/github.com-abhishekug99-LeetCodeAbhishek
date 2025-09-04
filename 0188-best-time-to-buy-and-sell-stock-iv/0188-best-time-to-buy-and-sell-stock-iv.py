class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n =len(prices)
        if n<=1:
            return 0
        
        # if k>=n//2: # if k is very large , its same as unlimited transactions
        #     profit=0
        #     for i in range(1, n):
        #         if prices[i]>prices[i-1]:
        #             profit+= prices[i] - prices[i-1]
        #     return profit

        dp = [[0] * n for _ in range(k+1)]
        for t in range(1,k+1):
            maxDiff = -prices[0]
            for d in range(1,n):
                dp[t][d] = max(dp[t][d-1], prices[d]+maxDiff)
                maxDiff = max(maxDiff, dp[t-1][d] - prices[d])
        return dp[k][n-1]

            
        
        # Works but con complete solution
        # if len(prices) ==1:
        #     return 0
         

        # dp = [[0] * len(prices) for _ in range(len(prices))]
        # profits = []
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[i]<prices[j]:
        #             dp[i][j] = prices[j]-prices[i]
        #             # profits.append(prices[j]-prices[i])
    
        
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if dp[i][j] > 0:
        #             profits.append(dp[i][j])
        # print(dp)
        # profits.sort(reverse = True)
        # print(profits)
        # return sum(profits[:k])
        
        
        


