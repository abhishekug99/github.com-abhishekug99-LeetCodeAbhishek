class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        preSum = 0
        preSumDict = defaultdict(int)
        preSumDict[0] = 1
        i = 0
        cnt = 0
        while i< len(nums):
            preSum +=nums[i]
            if (preSum-k) in preSumDict:
                cnt+=preSumDict[preSum-k]
            preSumDict[preSum]+=1
            i+=1
        return cnt

        
        # Correct but time limit exceeded
        # cnt = 0
        # subSum = 0
        # for i in range(len(nums)):
        #     subSum = 0
        #     j=i
        #     while j<len(nums):
        #         subSum += nums[j]
        #         if subSum ==k:
        #             cnt+=1
                    
        #         j+=1
        
        # return cnt            