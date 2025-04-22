class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxNum = max(nums)
        return nums.index(maxNum)
            