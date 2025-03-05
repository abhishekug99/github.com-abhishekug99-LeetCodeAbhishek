class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        noZeros = 0
        maxWind = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r]==0:
                noZeros+=1

            while noZeros>k:
                if nums[l] == 0:
                    noZeros-=1
                l+=1
            
            w = r - l + 1
            maxWind = max(maxWind, w)
        return maxWind
            



        