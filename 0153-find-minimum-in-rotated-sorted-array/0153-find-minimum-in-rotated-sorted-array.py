class Solution:
    def findMin(self, nums: List[int]) -> int:
        #just this will work too
        #return min(nums) ->O(n)

        #most optimal O(logn)
        l,r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]
        
        # bruteforce
        # finalMin = nums[0]
        # for num in nums:
        #     finalMin = min(num, finalMin)
        # return finalMin