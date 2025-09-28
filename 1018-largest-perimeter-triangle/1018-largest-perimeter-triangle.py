class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxPerimeter = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            print(i)
            if nums[i-2]+nums[i-1]>nums[i]:
                return nums[i-2]+nums[i-1]+nums[i]

        return 0

        
        # for r in range(len(nums)-1,-1,-1):
        #     l,j = 0, r-1
        #     while l<j:
        #         if nums[l]+nums[j]>nums[r]:
        #             perimeter = nums[l]+nums[j]+nums[r]
        #             print(perimeter)
        #             maxPerimeter = max(perimeter, maxPerimeter)
        #             j-=1
        #         else:
        #             l+=1
        # return maxPerimeter
        