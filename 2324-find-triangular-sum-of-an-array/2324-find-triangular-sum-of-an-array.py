class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        dp = [[0] * len(nums) for _ in range(len(nums)-1)]

        for i in range(len(nums)-1):
            curSum = nums[i]+nums[i+1]
            dp[0][i] = curSum%10
        
        for i in range(1, len(dp)):
            for j in range(len(nums)-i-1):
                currSum = dp[i-1][j] + dp[i-1][j+1]
                dp[i][j] = currSum%10
                # print(currSum)
                # if currSum<10:
                #     dp[i][j] = currSum 
                # elif currSum==10:
                #     dp[i][j] = 0
                # else:
                #     dp[i][j] = currSum%10 
        # print(dp)
        return dp[len(nums)-2][0]
        # return dp[-1][0]+dp[-1][1]