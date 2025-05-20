class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta = [0] * (n + 2)  

        for l, r in queries:
            delta[l] += 1
            delta[r + 1] -= 1

        opportunities = [0] * n
        curr = 0
        for i in range(n):
            curr += delta[i]
            opportunities[i] = curr

        for i in range(n):
            if nums[i] > opportunities[i]:
                return False  
        return True

        # n = len(nums)
        # need = nums[:]  
        # for l, r in queries:
        #     for i in range(l, r + 1):
        #         if need[i] > 0:
        #             need[i] -= 1  

        # return all(x == 0 for x in need)
        # return True

        # correct but bruteforce
        # for i in range(len(queries)):
        #     j = queries[i][0]
        #     k = queries[i][1]

        #     while j<=k:
        #         if nums[j]>0: 
        #             nums[j] -= 1
        #         j+=1
        
        # print(nums)
        # if sum(nums) == 0:
        #     return True
        # return False