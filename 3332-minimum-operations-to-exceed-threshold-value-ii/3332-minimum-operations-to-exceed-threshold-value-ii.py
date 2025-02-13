from itertools import combinations
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # creating binary  with root is smallest number
        print(nums)
        cnt = 0
        while nums[0]<k:
            if len(nums)<2:
                return -1
            x = heapq.heappop(nums) # remove the smallest
            y= heapq.heappop(nums) #remove the second smallest
            updateVal = x*2+y
            heapq.heappush(nums,updateVal)
            cnt+=1
        return cnt