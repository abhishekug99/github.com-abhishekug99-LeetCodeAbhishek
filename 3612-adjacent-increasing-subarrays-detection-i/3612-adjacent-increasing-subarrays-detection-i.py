class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        def checkIncreasingOrder(subArr: List[int])->bool:
            n = len(subArr)
            if n==1 and k==1:
                return True
            if n==1 and k!=1:
                return False
            for i in range(1, n):
                if subArr[i-1]>=subArr[i]:
                    return False
            return True


        for i in range(len(nums)-k):
            if (nums[i:i+k] and nums[i+k:i+k+k]) and (len(nums[i:i+k])==len(nums[i+k:i+k+k])):

                if checkIncreasingOrder(nums[i:i+k]) and checkIncreasingOrder(nums[i+k:i+k+k]):
                    # print(nums[i:i+k])
                    # print(nums[i+k:i+k+k])
                    return True
            else:
                continue
        return False
