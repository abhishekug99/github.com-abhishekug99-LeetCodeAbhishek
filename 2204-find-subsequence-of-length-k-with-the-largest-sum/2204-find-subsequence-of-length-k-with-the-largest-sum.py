class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        i=0
        res = []
        while i<len(nums):
            if len(res)!=k:
                res.append(nums[i])
            
            else:
                curSum = sum(res)
                minVal = min(res)
                if curSum - minVal+nums[i]>curSum:
                    res.pop(res.index(minVal))
                    res.append(nums[i])

            i+=1
        return res
            
        
