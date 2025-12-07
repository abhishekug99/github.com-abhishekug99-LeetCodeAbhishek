class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high+1)//2)-(low//2)
        
        res =0
        if low%2 or high%2:
            res+=1
        res+=(high-low)//2
        return res