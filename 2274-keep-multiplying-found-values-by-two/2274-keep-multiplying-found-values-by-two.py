class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original*=2
            if original not in nums:
                break
        return original