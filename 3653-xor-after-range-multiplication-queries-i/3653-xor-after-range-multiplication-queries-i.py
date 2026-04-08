class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        for i in range(len(queries)):
            li,ri,ki,vi = queries[i]
            idx = li
            while idx<=ri:
                nums[idx] = (nums[idx]*vi)%MOD
                idx+=ki
            
        res=nums[0]
        for i in range(1, len(nums)):
            res^=nums[i]
        
        return res
