class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        combinations = itertools.product('01', repeat=len(nums[0]))
        # print(list(combinations))
        for tup in combinations:
            if ''.join(tup) not in nums:
                return ''.join(tup)
    