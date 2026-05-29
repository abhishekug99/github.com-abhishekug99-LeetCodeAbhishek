class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            strn = str(n)
            if len(strn)>1:
                strnl = list(strn)
                sumn = sum(map(int, strnl))
                nums[i] = sumn
            else:
                continue
        return min(nums)