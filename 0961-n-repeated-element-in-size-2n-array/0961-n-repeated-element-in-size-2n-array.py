class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(set(nums))
        cnts = Counter(nums)
        # print(cnts)
        for k,v in cnts.items():
            if v==n-1:
                return k

        