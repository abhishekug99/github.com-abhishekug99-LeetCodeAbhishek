class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt+=1
                maxOnes = max(cnt, maxOnes)
            else:
                cnt = 0
            
            # if nums[i] == 1:
            #     j=i
            #     cnt = 0
            #     while nums[j]==1 and j<len(nums):
            #         cnt+=1
            #         j+=1
            #     maxOnes = max(maxOnes, cnt)
            #     i=j
        return maxOnes

