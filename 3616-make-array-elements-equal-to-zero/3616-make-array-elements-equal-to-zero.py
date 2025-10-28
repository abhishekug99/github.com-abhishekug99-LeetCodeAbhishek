class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        res = 0
        l =0

        for num in nums:
            if num!=0:
                l+=num
            else:
                r = s-l
                if l==r:
                    res+=2
                elif abs(l-r)==1:
                    res+=1
        return res    
        
            
