class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [1]*n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        
        
        

        # for i in range(len(nums)):
        #     if nums[i] == nums[-1]:
        #         prdt = math.prod(nums[:-1])
        #         res.append(prdt)
        #     else:
        #         prevPrdt = prod(nums[:i])
        #         postPrdt = prod(nums[i+1:])
        #         res.append(prevPrdt*postPrdt)
        return res
