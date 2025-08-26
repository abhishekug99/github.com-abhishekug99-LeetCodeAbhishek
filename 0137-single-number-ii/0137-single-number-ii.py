class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #bit manupulation with XOR
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

        #normal
        # cntMap = {}
        # for i in range(len(nums)):
        #     if nums[i] not in cntMap:
        #         cntMap[nums[i]] =1
        #     else:
        #         cntMap[nums[i]] += 1
        # for k,v in cntMap.items():
        #     if v ==1:
        #         return k
        #         break