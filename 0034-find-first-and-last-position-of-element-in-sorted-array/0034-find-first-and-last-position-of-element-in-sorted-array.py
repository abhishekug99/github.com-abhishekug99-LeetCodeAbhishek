class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if target not in nums:
            return[-1,-1]
        
        l,r = 0, len(nums)-1
        i=-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                i=mid
                # print(res)
                break
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        if i==-1:
            return[-1,-1]
        left ,right= i,i
        while left>0 and nums[left-1]==target:
            left -=1
        while right<len(nums)-1 and nums[right+1] == target:
            right+=1
        

        return [left,right]