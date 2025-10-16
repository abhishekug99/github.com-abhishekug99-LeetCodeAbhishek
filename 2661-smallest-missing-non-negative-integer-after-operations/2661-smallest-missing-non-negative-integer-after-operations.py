class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        cnts=[0]*value
        for num in nums:
            cnts[num%value]+=1
        mex = 0
        while True:
            r = mex%value
            if cnts[r] ==0:
                return mex
            cnts[r]-=1
            mex+=1
        
            
        #     if nums[i] ==0 :
        #         continue
        #     if nums[i]>0:
        #         if abs(nums[i]-value) >= value or nums[i]==value:
        #             cnt+=1
        #             while nums[i]<= value:
        #                 nums[i]-=value
        #     elif nums[i]<0:
        #         if abs(-nums[i]-value) >= value or nums[i]==value:
        #             cnt+=1
        #             while nums[i]>= value:
        #                 nums[i]+=value
        # return cnt


        