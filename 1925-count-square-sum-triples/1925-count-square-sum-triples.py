class Solution:
    def countTriples(self, n: int) -> int:
        if n<3:
            return 0
        nums = [i for i in range(1,n+1)]
        combs = list(combinations(nums,2))
        res = 0
        for a,b in combs:
            c2 = a**2 + b**2
            c = int(c2**0.5)
            if c*c == c2 and c<=n:
                res+=2
        return res
        