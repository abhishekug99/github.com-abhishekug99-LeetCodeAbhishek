import numpy
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        dp = [[float('-inf')]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                currProd = nums1[i]*nums2[j]
                if dp[i+1][j+1]>0:
                    currProd+=dp[i+1][j+1]
                skip1 = dp[i+1][j]
                skip2 = dp[i][j+1]
                dp[i][j] = max(currProd, skip1, skip2)
        return dp[0][0]
        


