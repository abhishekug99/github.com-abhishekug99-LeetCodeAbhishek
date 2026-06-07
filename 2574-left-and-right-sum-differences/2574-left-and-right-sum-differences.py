class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                res[i] = sum(nums[i+1:])
            elif i==len(nums)-1:
                res[i] = sum(nums[:i])
            else:
                res[i] = abs(sum(nums[i+1:])-sum(nums[:i]))
        
        return res