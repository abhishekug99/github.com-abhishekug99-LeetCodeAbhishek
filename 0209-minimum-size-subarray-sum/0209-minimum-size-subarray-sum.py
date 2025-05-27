class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #correct bruteforce but TLE O(n^2)
        if target in nums:
            return 1
        
        minDist = float('inf')
        curr = 0
        j = 0
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>=target: 
                minDist = min(minDist,i-j+1)
                curr-=nums[j]
                j+=1
        return minDist if minDist != float('inf') else 0


        