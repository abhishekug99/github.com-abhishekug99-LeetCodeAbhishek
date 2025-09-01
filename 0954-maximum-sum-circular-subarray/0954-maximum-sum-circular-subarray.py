class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #this is important to hande the all -ve array, can be handled in the output also
        # if max(nums)<0:
        #     return max(nums)
        
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0,0
        total=0

        for n in nums:
            curMax = max(curMax+n, n)
            curMin = min(curMin+n, n)
            total+=n
            globalMax = max(globalMax,curMax)
            globalMin = min(globalMin, curMin)
        
        # return max(globalMax, total-globalMin) 
        return max(globalMax, total-globalMin) if globalMax>0 else globalMax
