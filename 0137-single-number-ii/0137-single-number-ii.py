class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cntMap = {}
        for i in range(len(nums)):
            if nums[i] not in cntMap:
                cntMap[nums[i]] =1
            else:
                cntMap[nums[i]] += 1
        for k,v in cntMap.items():
            if v ==1:
                return k
                break