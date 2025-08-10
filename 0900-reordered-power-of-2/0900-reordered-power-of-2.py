class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        sig = Counter(s)
        
        L = len(s)
        i = 0
        while True:
            p = str(1 << i)   
            if len(p) > L:            
                break
            if len(p) == L and Counter(p) == sig:
                return True
            i += 1
        return False
        