class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #Buy
        r = 1 #Sell [1,2]
        finalProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                currProfit = prices[r] - prices[l] #our current Profit
                finalProfit =max(currProfit,finalProfit)
            else:
                l = r
            r += 1
        return finalProfit  