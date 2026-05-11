class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n > 9:
                n = str(n)
                nl = list(n)
                nl = [int(a) for a in nl]
                res += nl
            else:
                res.append(n)

        return res