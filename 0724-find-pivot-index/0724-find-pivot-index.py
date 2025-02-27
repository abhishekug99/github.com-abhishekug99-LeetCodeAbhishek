class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            rSum = total-lSum-nums[i]
            if lSum == rSum:
                return i
            lSum += nums[i]            
        
        return -1

            