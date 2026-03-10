class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0]*(zero+1) for _ in range(one+1)]
        dp1 = [[0]*(zero+1) for _ in range(one+1)]

        for j in range(1, min(limit, zero)+1):
            dp0[0][j] = 1

        for i in range(1, min(limit, one)+1):
            dp1[i][0] = 1

        for i in range(1, one+1):
            for j in range(1, zero+1):

                dp0[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j - limit - 1 >= 0:
                    dp0[i][j] = (dp0[i][j] - dp1[i][j-limit-1]) % MOD

                dp1[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i - limit - 1 >= 0:
                    dp1[i][j] = (dp1[i][j] - dp0[i-limit-1][j]) % MOD

        return (dp0[one][zero] + dp1[one][zero]) % MOD
        
        # MOD = 10**9+7
        # t = [[[-1 for _ in range(2)] for _ in range(zero+1)] for _ in range(one+1)]
        # def solve(onesLeft, zerosLeft, lastWasOne, limit):
        #     if onesLeft == 0 and zerosLeft == 0:
        #         return 1
        #     if t[onesLeft][zerosLeft][lastWasOne] != -1:
        #         return t[onesLeft][zerosLeft][lastWasOne]
            
        #     res=0 
        #     if lastWasOne:
                
        #         for l in range(1, min(limit, zerosLeft) + 1):
        #             res = (res + solve(onesLeft, zerosLeft - l, 0, limit)) % MOD
        #     else:
            
        #         for l in range(1, min(limit, onesLeft) + 1):
        #             res = (res + solve(onesLeft - l, zerosLeft, 1, limit)) % MOD
        #     t[onesLeft][zerosLeft][lastWasOne] = res
        #     return res
        
        # startwithone = solve(one, zero, 0, limit)
        # startwithzero = solve(one, zero, 1, limit)

        # return (startwithone + startwithzero) % MOD