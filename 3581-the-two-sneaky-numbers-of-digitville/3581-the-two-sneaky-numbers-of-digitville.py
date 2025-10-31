class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numCnts = Counter(nums)
        res = []
        for k, v in numCnts.items():
            if v == 2:
                res.append(k)

        return res