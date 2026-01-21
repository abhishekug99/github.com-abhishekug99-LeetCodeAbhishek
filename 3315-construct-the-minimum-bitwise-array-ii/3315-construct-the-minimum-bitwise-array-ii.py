class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # res=[-1]*n
        # for i in range(n):
        #     for j in range(0,nums[i]+1):
        #         if j|(j+1)==nums[i]:
        #             res[i]=j
        #             break
        # return res

        #optimal
        res = []
        for num in nums:
            if num==2:
                res.append(-1)
                continue
            if num%2==0:
                res.append(-1)
                continue
            bit=1
            while num & bit:
                bit<<=1
            lead1 = bit>>1
            res.append(num-lead1)
        return res