class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        currSum = sum(nums)
        remain = sum(nums)%p
        if not remain:
            return 0 
        if remain in nums:
            return 1
        res = float('inf')
        prefix = 0
        mp = {0:-1}
        for i, num in enumerate(nums):
            prefix = (prefix+num)%p
            target = (prefix-remain)%p
            if target in mp:
                res = min(res, i-mp[target])
            mp[prefix]=i
        return res if res<len(nums) else -1
        # return -1