class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res=[]
        i=0

        while i< len(nums):
            s=nums[i]
            j=i
            while j+1<len(nums) and nums[j+1] == nums[j]+1:
                j+=1
            if s==nums[j]:
                res.append(str(s))
            else:
                res.append(f"{s}->{nums[j]}")
            i=j+1

        return res
