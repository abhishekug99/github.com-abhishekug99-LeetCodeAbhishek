class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        res = []
        queue = deque()
        l=r=0
        while r<len(nums):
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)

            if l>queue[0]:
                queue.popleft()
            if (r+1)>=k:
                res.append(nums[queue[0]])
                l+=1
            r+=1
        return res
        
        # O(n*k)
        # res = []
        # if len(nums) ==1:
        #     return nums
        # j = k-1
        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        
        # return res