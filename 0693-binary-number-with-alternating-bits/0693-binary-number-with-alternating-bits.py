class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nBits = bin(n)[2:]
        print(nBits)
        if len(nBits)==1:
            return True
            
        if all(b == '1' for b in nBits) or all(b == '0' for b in nBits):
            return False
        
        for i in range(1, len(nBits)):
            if nBits[i] != nBits[i-1]:
                continue
            else:
                return False
        return True