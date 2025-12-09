class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9+7
        freqs = {}
        numPartial = {}
        for num in nums:
            freqs[num] = freqs.get(num,0)+1
        
        res = 0
        for num in nums:
            goal = num*2
            left = numPartial.get(goal,0)
            numPartial[num] = numPartial.get(num,0)+1
            right = freqs.get(goal, 0) - numPartial.get(goal,0)
            res = (res + left*right)%MOD

        return res




        # idxs = [i for i in range(n)]
        # combs = list(combinations(idxs,3))
        # print(combs)
        # for i,j,k in combs:
        #     if nums[i] == nums[j]*2 and nums[k] == nums[j]*2:
        #         res+=1
        #     else: continue
        # return res
         


        #correct #TLE
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1,n):
        #             if nums[i] == nums[j]*2 and nums[k] == nums[j]*2:
        #                 res+=1
        #             else: continue
        # return res%MOD
