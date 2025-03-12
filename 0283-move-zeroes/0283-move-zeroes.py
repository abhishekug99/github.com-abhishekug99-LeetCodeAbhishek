class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            nums
    
        n = len(nums)
        
        for i in range(n):
            if nums[i]==0:
                nums.append(nums.pop(nums.index(nums[i])))
        
        