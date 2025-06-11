class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        # j = 0
        # O(n^2) not that worthy
        # if len(nums)==0:
        #     return 0
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j]<nums[i]:
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)

        #
        seq = []
        for num in nums:
            i = bisect.bisect_left(seq,num)
            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = num

        return len(seq)

        # for i in range(len(nums)):
        #     j=i+1
        #     cur = nums[i]
        #     start = nums[i]
        #     while j< len(nums):
        #         if nums[j]>cur:
        #             dp[i]+=1
        #             cur = nums[j]
        #         elif nums[j]<cur and nums[j]>start:
        #             cur =  nums[j]
        #         j+=1

        # return max(dp)