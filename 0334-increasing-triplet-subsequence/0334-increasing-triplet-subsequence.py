class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for all kind of numbers
        f = float('inf')
        s = float('inf')

        for num in nums:
            if num <= f:
                f = num  # Smallest till now
            elif num <= s:
                s = num  # Second till now
            else:
                return True  # Found a triplet: first < second < num

        return False
        
        # only for consecutive
        # cnt =0
        # for i in range(1, len(nums)-1):
        #     if nums[i]>nums[i-1] and nums[i]<nums[i+1]:
        #         cnt+=1
        # if cnt>0:
        #     return True
        
        # return False
        