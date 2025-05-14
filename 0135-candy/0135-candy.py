class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp = [1]*(len(ratings))

        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]: 
                dp[i] = dp[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                dp[i] = max(dp[i],dp[i+1]+1)
        return sum(dp)
        
        # approach is partially correct but can't as it goin through one pass, 20/49, need to do one forwARD PASS AND REVERE PASS
        # dp = [1]*(len(ratings))
        # # dp[0] = 1
        # newMin = 1
        # for i in range(1,len(ratings)):
        #     if ratings[i-1]<ratings[i]: 
        #         dp[i] = dp[i-1]+1
            
        #     if ratings[i-1]>= ratings[i]:
        #         if dp[i]>1:
        #            dp[i]-=1
        #         elif ratings[i-1]>ratings[i]:
        #             dp[i-1]+=1
        #         else:
        #             dp[i] = 1
        # print(dp)
        # return sum(dp)


