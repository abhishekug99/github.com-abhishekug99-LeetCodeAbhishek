class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp Approach
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        dp = [0]*len(nums)
        dp[0] = nums[0] 
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

        #most efficient
        # r1, r2 = 0,0
        # for n in nums:
        #     tmp = max(n+r1,r2)
        #     r1 = r2
        #     r2 = tmp
        # return r2
        
        
        # sum1 = 0
        # sum2 = 0
        # if len(nums)<=2:
        #     return max(nums)
    
        # for i in range(len(nums)):
        #     if i%2==0: 
        #         sum1 = nums[i] + sum1
        #     else:
        #         print(i)
        #         sum2 = nums[i] + sum2
        # print(sum1,sum2)

        # return max(sum1, sum2)

        