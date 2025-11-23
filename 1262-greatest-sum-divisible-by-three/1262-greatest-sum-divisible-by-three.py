class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        if len(nums)==1 and nums[0]%3!=0:
            return 0
        res = 0
        numsSum = sum(nums)

        if numsSum%3 == 0:
            return  numsSum
        
        mod1 = []
        mod2 = []
        for n in nums:
            if n%3 ==1:
                mod1.append(n)
            elif n%3 ==2:
                mod2.append(n)
        mod1.sort()
        mod2.sort()
        if numsSum%3==1:
            if mod1:
                res = max(res, numsSum - mod1[0])
            if len(mod2)>=2:
                res = max(res, numsSum - mod2[0]-mod2[1])
        else:
            if mod2:
                res = max(res, numsSum - mod2[0])
            if len(mod1)>=2:
                res = max(res, numsSum - mod1[0]-mod1[1])
        return res
