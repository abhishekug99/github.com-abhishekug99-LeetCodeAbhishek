class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1]*len(prices)

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1]-1:
                dp[i] += dp[i-1]
            else:
                continue
        return sum(dp)
        # print(dp)
        # res=0
        # for i in range(1, len(dp)):
        #     if dp[i]<dp[i-1]:
        #         res+= (dp[i-1]*(dp[i-1]+1))//2
        
        # res = res + (dp[-1]*(dp[-1]+1))//2

        # return len(prices) if 2 not in dp else res

            

    
        # return len(prices)+max(dp) if max(dp)!=1 else len(prices)

