class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n= len(prices)
        totalprofits = [0]*(n+1)
        priceSum = [0]*(n+1)

        for i in range(n):
            totalprofits[i+1] = totalprofits[i] + prices[i]*strategy[i] 
            priceSum[i+1] = priceSum[i]+prices[i]
        
        res = totalprofits[n]
        for i in range(k-1,n):
            lprofit = totalprofits[i-k+1]
            rprofit = totalprofits[n]-totalprofits[i+1]
            changedprofit = priceSum[i+1]-priceSum[i-k // 2+1]
            res = max(res, lprofit + changedprofit + rprofit)
        return res