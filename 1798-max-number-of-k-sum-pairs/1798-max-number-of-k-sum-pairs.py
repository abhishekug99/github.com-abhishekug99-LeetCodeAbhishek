class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt=0
        i, j  = 0, len(nums)-1
        nums.sort()
        while i < j:
            currSum = nums[i] + nums[j]

            if currSum == k:
                cnt+=1
                i+=1
                j-=1
            if currSum > k:
                j-=1
            if currSum < k:
                i+=1
           
        return cnt

        