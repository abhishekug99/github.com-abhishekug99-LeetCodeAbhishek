class Solution:
    def concatenatedBinary(self, n: int) -> int:
        resBin = ''
        for num in range(1, n+1):
            resBin += bin(num)[2:]
        
        return int(resBin,2) % (10**9+7)