class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Optimum dp O(n)
        n = len(energy)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            dp[i] = energy[i]
            if i+k<n:
                dp[i]+=dp[i+k]
        return max(dp)

        #TLE O(n^2)
        # maxEnergy = -math.inf
        # n = len(energy)

        # for i in range(n):
        #     curEnergy = 0
        #     j = i
        #     while j < n:
        #         curEnergy += energy[j]
        #         j += k
        #     maxEnergy = max(maxEnergy, curEnergy)

        # return maxEnergy