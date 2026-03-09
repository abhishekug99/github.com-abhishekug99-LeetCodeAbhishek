class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9+7
        t = [[[-1 for _ in range(2)] for _ in range(201)] for _ in range(201)]
        def solve(onesLeft, zerosLeft, lastWasOne, limit):
            if onesLeft == 0 and zerosLeft == 0:
                return 1
            if t[onesLeft][zerosLeft][lastWasOne] != -1:
                return t[onesLeft][zerosLeft][lastWasOne]
            
            res=0 
            if lastWasOne:
                
                for l in range(1, min(limit, zerosLeft) + 1):
                    res = (res + solve(onesLeft, zerosLeft - l, 0, limit)) % MOD
            else:
            
                for l in range(1, min(limit, onesLeft) + 1):
                    res = (res + solve(onesLeft - l, zerosLeft, 1, limit)) % MOD
            t[onesLeft][zerosLeft][lastWasOne] = res
            return res
        
        startwithone = solve(one, zero, 0, limit)
        startwithzero = solve(one, zero, 1, limit)

        return (startwithone + startwithzero) % MOD