class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        powerOfTwos = [1]*(len(nums))
        MOD = 10**9+7

        for i in range(1,len(nums)):
            powerOfTwos[i] = (powerOfTwos[i-1]*2)%MOD
        cnt = 0
        while l<=r:
            if nums[l] + nums[r]<=target:
                cnt = (cnt + powerOfTwos[r-l])%MOD
                l+=1
            else:
                r-=1
        return cnt
        # cnt = 0
        # for i in range(len(nums)):
            
        #     temp = []
        #     temp.append(nums[i])
        #     if (nums[i]*2)<=target:
        #         cnt+=1
        #     if len(temp)>1:
        #         minVal = min(temp)
        #         maxVal = max(temp)
        #         if maxVal + maxVal<=target:
        #             cnt+=1
        #         elif maxVal + maxVal>target:
        #             temp.pop(maxVal.index) 
        
        # return cnt%(10**9+9)

        
            