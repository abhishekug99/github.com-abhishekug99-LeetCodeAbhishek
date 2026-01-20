class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
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