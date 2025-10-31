class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        rep = set()
        for num in nums:
            if num not in rep:
                rep.add(num)
            else:
                res.append(num)
        return res
        # numCnts = Counter(nums)
        # res = []
        # for k, v in numCnts.items():
        #     if v == 2:
        #         res.append(k)

        # return res