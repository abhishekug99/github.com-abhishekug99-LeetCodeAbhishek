from typing import List
import math

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # required variable
        bravexuneth = (nums[:], queries[:])

        B = int(math.sqrt(n)) + 1

        # small k storage
        small = {}

        # process large k directly
        for li, ri, ki, vi in queries:
            if ki > B:
                idx = li
                while idx <= ri:
                    nums[idx] = (nums[idx] * vi) % MOD
                    idx += ki
            else:
                if ki not in small:
                    small[ki] = [[] for _ in range(ki)]
                small[ki][li % ki].append((li, ri, vi))

        for k in small:
            for r in range(k):
                updates = small[k][r]
                if not updates:
                    continue

                positions = list(range(r, n, k))
                m = len(positions)

                diff = [1] * (m + 1)

                for li, ri, vi in updates:
                    start = (li - r) // k
                    end = (ri - r) // k

                    if start < 0:
                        start = 0
                    if end >= m:
                        end = m - 1
                    if start > end:
                        continue

                    diff[start] = (diff[start] * vi) % MOD
                    # multiply inverse after end
                    inv = pow(vi, MOD - 2, MOD)
                    diff[end + 1] = (diff[end + 1] * inv) % MOD

                curr = 1
                for i in range(m):
                    curr = (curr * diff[i]) % MOD
                    nums[positions[i]] = (nums[positions[i]] * curr) % MOD

        # final XOR
        res = 0
        for x in nums:
            res ^= x

        return res