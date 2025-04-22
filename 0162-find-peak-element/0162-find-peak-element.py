class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Most Optimal LOL
        # maxNum = max(nums)
        # return nums.index(maxNum)
        
        # l, r = 0, len(nums)-1
        # while l<r:
        #     mid = (l+r)//2
            
        #     if nums[mid] < nums[mid+1]:
        #         l = mid+1
            
        #     else:
        #         r = mid
        
        # return l
        
        #HeapApproach
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))

        return heapq.heappop(heap)[1]



