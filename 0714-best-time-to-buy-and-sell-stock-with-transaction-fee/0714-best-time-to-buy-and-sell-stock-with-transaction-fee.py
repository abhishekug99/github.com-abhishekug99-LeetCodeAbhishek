class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp-most optimal
        cash = 0
        hold = -prices[0]

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)
            print(cash)
            hold = max(hold, cash - price)
            print(hold)
        return cash
        
        #dfs
        # dp = {} #key (i,buy), val = maxprofit
        # def dfs(i, buying):

        #     if i==len(prices):
        #         return 0

        #     if (i, buying) in dp:
        #         return dp[(i, buying)]

        #     if buying:
        #         buy = dfs(i+1, False) - prices[i]
        #         skip  = dfs(i+1,True)
        #         dp[(i, buying)] = max(buy, skip)
            
        #     else:
        #         sell = dfs(i+1, True) + prices[i] - fee
        #         hold = dfs(i+1, False)
        #         dp[(i, buying)] = max(sell,hold)
            
        #     return dp[(i, buying)]
        

        # return dfs(0,True)
            
          