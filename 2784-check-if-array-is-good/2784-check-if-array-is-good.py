class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1   
        
        cnts = Counter(nums)
        
        if len(cnts) != n:
            return False
        
        for i in range(1, n):
            if cnts[i] != 1:
                return False
        
        if cnts[n] != 2:
            return False
        
        return True