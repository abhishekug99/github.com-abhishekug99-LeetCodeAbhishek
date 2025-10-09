class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        if n == 0 or m == 0:
            return 0
        PS = [0]*n
        s=0
        for i, x in enumerate(skill):
            s+=x
            PS[i] = s
        def gap(jm1, j):
            best = PS[0]*mana[jm1] - 0*mana[j]
            for i in range(1,n):
                cand = PS[i]*mana[jm1] - PS[i-1]*mana[j]
                if cand> best:
                    best = cand
            return best
        
        start = 0
        for j in range(1,m):
            start+=gap(j-1,j)
        
        total_last = PS[-1]*mana[-1]
        return start+total_last


        # dp = [[0]*m for _ in range(n)]
        
        # dp[0][0] = skill[0] * mana[0]

        # for j in range(1, m):
        #     dp[0][j] = dp[0][j-1] + skill[0] * mana[j]

        # for i in range(1, n):
        #     dp[i][0] = dp[i-1][0] + skill[i] * mana[0]

        # for i in range(1,n):
        #     for j in range(1,m):
        #         dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + skill[i]*mana[j]
        # print(dp)
        # return dp[-1][-1]

    
    