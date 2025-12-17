class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[-inf]*3 for _ in range(k+1)]
        dp[0][0]=0
        # 0 to free,1 to hold buy, 2 hold short
        # print(dp)
        for price in prices:
            tmpdp = [row[:] for row in dp]
            for t in range(k+1):
                #handling free state
                if dp[t][0]!= -inf:
                    tmpdp[t][1] = max(tmpdp[t][1], dp[t][0]-price)
                    tmpdp[t][2] = max(tmpdp[t][2], dp[t][0]+price)
                #handling buy to sell normal
                if t<k and dp[t][1] != -inf:
                    tmpdp[t+1][0]=max(tmpdp[t+1][0], dp[t][1]+price)
                # handling short buy back
                if t<k and dp[t][2] != -inf:
                    tmpdp[t+1][0]=max(tmpdp[t+1][0], dp[t][2]-price)
            dp = tmpdp
        print(dp)
        return max(dp[t][0] for t in range(k+1))