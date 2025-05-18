class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        for num in nums:
            if num == 0:
                red.append(num)
            elif num ==1:
                white.append(num)
            else:
                blue.append(num)
        numsSort = red + white + blue
        print(numsSort)
        for i in range(len(nums)):
            nums[i] = numsSort[i]
        