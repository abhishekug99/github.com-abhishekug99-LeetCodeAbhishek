class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False]*len(nums)
        bistr = ''
        for i in range(len(nums)):
            bistr+=str(nums[i])
            if int(bistr, 2)%5 == 0:
                res[i] = True
            else:
                continue
        return res 
        