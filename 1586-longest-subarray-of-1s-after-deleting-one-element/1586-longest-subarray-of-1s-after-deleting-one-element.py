class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        win = 0
        cnt = 0
        l = 0
        if 0 not in nums:
            return len(nums)-1
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt+=1
            
            while cnt>1:
                if nums[l] == 0:
                    cnt-=1
                l+=1
            
            w = r-l
            
            win=max(win,w)
        return win




        

