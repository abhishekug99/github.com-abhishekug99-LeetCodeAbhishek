class Solution:
    def numSub(self, s: str) -> int:
        # '0110111'
        MOD = 10**9 + 7
        res = 0
        consec = 0

        for i in range(len(s)):
            if s[i] == '1':
                consec+=1
            elif s[i] == '0':
                consec = 0
            res+=consec

        return res%MOD
    
    
