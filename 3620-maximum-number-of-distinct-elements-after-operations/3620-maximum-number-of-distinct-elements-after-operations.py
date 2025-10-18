class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        usedCnt = 0
        nxtAvailable = -10**18

        for num in nums:
            l,h=num-k, num+k
            if h<nxtAvailable:
                continue
            assignedVal = max(l, nxtAvailable)
            usedCnt+=1
            nxtAvailable = assignedVal+1
        return usedCnt
        
        #TLE nlogn
        # nums.sort()
        # notnew = set()
        # for num in nums:
        #     for j in range(-k, k+1):
        #         c = num+j
        #         if c not in notnew:
        #             notnew.add(c)
        #             break
        # return len(notnew)


        #works but one issue
        # for i in range(len(nums)):
        #     j=-k
        #     while j<=k:
        #         if nums[i] + j not in nums:
        #             nums[i] = nums[i] + j
        #             break
        
        #         j+=1
        # print(nums)
        # num = set(nums)
        # return len(num) 