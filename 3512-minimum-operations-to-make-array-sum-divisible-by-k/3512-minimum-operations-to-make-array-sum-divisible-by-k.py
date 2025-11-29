class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        currSum = sum(nums)
        return currSum%k
        # res = 0
        # while currSum%k!=0:
        #     currSum-=1
        #     res+=1
        # return res