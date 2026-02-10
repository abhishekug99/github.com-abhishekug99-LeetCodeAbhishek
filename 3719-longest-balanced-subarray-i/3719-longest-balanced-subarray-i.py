class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            odd = set()
            even = set()
            if nums[i]%2==0:
                even.add(nums[i])
            else:
                odd.add(nums[i])
            for j in range(i+1, len(nums)):
                if nums[j]%2==0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    res = max(res, j-i+1)
                
        return res