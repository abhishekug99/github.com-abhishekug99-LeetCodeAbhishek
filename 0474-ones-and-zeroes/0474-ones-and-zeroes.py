from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = [(s.count('0'), s.count('1')) for s in strs]

        @lru_cache(None)
        def dfs(i, zeros, ones):
            if i ==len(strs):
                return 0
            z,o = cnts[i]
            res = dfs(i+1, zeros, ones)
            if zeros+z<=m and ones+o<=n:
                res = max(res, 1 + dfs(i+1, zeros+z, ones+o))
            return res

        return dfs(0,0,0)

        