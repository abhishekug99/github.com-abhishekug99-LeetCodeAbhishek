class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        numOperations = min(numOperations, n)  # safe cap

        ans = 1
        i = 0
        while i < n:
            v = nums[i]
            j = i
            while j < n and nums[j] == v:
                j += 1
            cnt_v = j - i  

            L = bisect_left(nums, v - k)
            R = bisect_right(nums, v + k)  
            in_ball = R - L               

            ops_needed = in_ball - cnt_v   
            if ops_needed <= numOperations:
                ans = max(ans, in_ball)
            else:
                ans = max(ans, cnt_v + numOperations)

            i = j

        left = 0
        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            window = right - left + 1
            ans = max(ans, min(window, numOperations))

        return min(ans, n)

    # def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
    #     nums.sort()
    #     n = len(nums)
    #     if n==0:
    #         return 0
        
    #     maxFreq = 0
    #     left = 0

    #     while left<n:
    #         target = nums[left]
    #         right = left
    #         while right < n and nums[right] == target:
    #             right+=1
    #         initialCnt = right-left
    #         leftBound = target-k
    #         rightBound = target+k

    #         startIdx = bisect_left(nums, leftBound)
    #         endIdx = bisect_right(nums, rightBound)

    #         potential = endIdx-startIdx
    #         convertible = potential - initialCnt
    #         opsToUse = min(numOperations, convertible)
    #         currFreq = initialCnt + opsToUse
    #         maxFreq = max(maxFreq, currFreq)
    #         left = right
    #     return maxFreq
