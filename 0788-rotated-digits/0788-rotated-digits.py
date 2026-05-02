class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0','1','2','5','6','8','9'}
        change = {'2','5','6','9'}
        
        def isGood(x):
            s = str(x)
            hasChange = False
            
            for ch in s:
                if ch not in valid:
                    return False
                if ch in change:
                    hasChange = True
            
            return hasChange
        
        cnt = 0
        for i in range(1, n+1):
            if isGood(i):
                cnt += 1
        
        return cnt