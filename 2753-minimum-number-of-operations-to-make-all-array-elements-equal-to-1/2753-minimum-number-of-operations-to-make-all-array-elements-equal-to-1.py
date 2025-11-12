class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def getGCD(a,b):
            while b:
                a,b = b, a%b
            return a
        
        n = len(nums)
        ones = nums.count(1)
        
        if ones>0:
            return n-ones
        
        minOps = float('inf')
        for i in range(n):
            g = nums[i] 
            for j in range(i+1,n):
                g = getGCD(g, nums[j])
                if g ==1:
                    minOps = min(minOps, j-i+1)
                    break
        if minOps == float('inf'):
            return -1
        
        return (minOps-1) + (n-1)


        #misses few edgw cases
        # res=0
        # for i in range(len(nums)-1):
        #     if getGCD(nums[i], nums[i+1]) == 1:
        #         print(i)
        #         nums[i] = 1
        #         res+=1
        # # print(nums)
        # if 1 not in nums:
        #     return -1
        
        # currOnes = nums.count(1)
        # res += len(nums)-currOnes

        # return res 

        


        

        # print(list(combs))
