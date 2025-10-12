class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        if m == 0:
            return 0 if k != 0 else 1  # empty sequence contributes 1 product (neutral)
        
        # Precompute binomials C up to m
        C = [[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        # Precompute powers nums[j]^c for c=0..m
        powv = [[1]*(m+1) for _ in range(n)]
        for j in range(n):
            v = nums[j] % MOD
            for c in range(1, m+1):
                powv[j][c] = (powv[j][c-1] * v) % MOD

        # dp[used][carry][ones] -> ways
        # Use sparse dicts to keep it fast.
        from collections import defaultdict
        dp = defaultdict(int)
        dp[(0, 0, 0)] = 1

        for j in range(n):
            newdp = defaultdict(int)
            # We will assign c copies of index j among the remaining (m - used).
            # Transition: (used, r, s) --choose c--> (used+c, (r+c)>>1, s + ((r+c)&1))
            for (used, r, s), ways in dp.items():
                rem = m - used
                if ways == 0 or rem == 0:
                    # Only c=0 possible if rem=0
                    if rem == 0:
                        r2 = r >> 1
                        s2 = s + (r & 1)
                        if s2 <= k:
                            newdp[(used, r2, s2)] = (newdp[(used, r2, s2)] + ways) % MOD
                    continue

                # Try all c from 0..rem
                # Early prune on ones: we never let ones exceed k.
                for c in range(rem + 1):
                    r_sum = r + c
                    s2 = s + (r_sum & 1)
                    if s2 > k:
                        continue
                    r2 = r_sum >> 1
                    add = ways * C[rem][c] % MOD * powv[j][c] % MOD
                    newdp[(used + c, r2, s2)] = (newdp[(used + c, r2, s2)] + add) % MOD
            dp = newdp

        # Finish: only used == m allowed; remaining carry's popcount contributes more ones
        def popcount(x: int) -> int:
            return x.bit_count()  # Python 3.8+: use bin(x).count("1") if older

        ans = 0
        for (used, r, s), ways in dp.items():
            if used != m:
                continue
            total_ones = s + popcount(r)
            if total_ones == k:
                ans = (ans + ways) % MOD
        return ans
        
        
        # n=len(nums)
        # maxMask = 1<< (n+m)
        # dp = [[0]*maxMask for _ in range(m+1)]
        # dp[0][0] = 1
        # MOD = 10**9 + 7

        # for i in range(m):
        #     for mask in range(maxMask):
        #         if dp[i][mask]==0:
        #             continue
        #         for j in range(n):
        #             newMask = mask + (1<<j)
        #             dp[i+1][newMask] = (dp[i+1][newMask]+dp[i][mask]*nums[j])%MOD
        # res=0
        # for mask in range(maxMask):
        #     if bin(mask).count("1")==k:
        #         res = (res + dp[m][mask])%MOD
        
        # return res
        
        
        #work well tle
        # n = len(nums)
        # allSeqs = list(product(range(n), repeat=m))
        # total =0
        # MOD = 10**9 + 7
        # for seq in allSeqs:
        #     powerSum = sum(2**i for i in seq)
        #     if bin(powerSum).count('1') == k:
        #         prodVal = 1
        #         for i in seq:
        #             prodVal = (prodVal*nums[i])%MOD
        #         total = (total+prodVal)%MOD
        
        # return total

        # print(allSeqs)
