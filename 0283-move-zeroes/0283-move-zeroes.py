class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #works well O(n)
        # if len(nums)==0:
        #     nums
    
        # n = len(nums)
        
        # for i in range(n):
        #     if nums[i]==0:
        #         nums.append(nums.pop(nums.index(nums[i])))

        #two pointers
        l = 0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
        
        
        