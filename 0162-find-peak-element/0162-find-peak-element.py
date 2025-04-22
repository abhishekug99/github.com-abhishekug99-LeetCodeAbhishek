class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[1]>nums[0]:
                return 1
            else:
                return 0
        l,r = 0,len(nums)-1
        maxNum = max(nums)
        # while l<=r:
        #     mid =(l+r)//2
        #     if maxNum<nums[mid]:
        #         l=mid+1
        #     elif maxNum>nums[mid]:
        #         r = mid-1
        #     else:
        #         return mid
        return nums.index(maxNum)
            