class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = 0
        
        for j in range(1, n):
            for i in range(j):
                if -target <= nums[j] - nums[i] <= target and dp[i] != -float('inf'):
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n-1] if dp[n-1] != -float('inf') else -1