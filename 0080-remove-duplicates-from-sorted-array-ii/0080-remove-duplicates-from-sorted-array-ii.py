class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        if not nums:
            return 0
        stackTop= 0
        for i in range(len(nums)):
            # res.append(nums[i])
            if stackTop<2 or nums[i]!=nums[stackTop-2]:
                # res.pop()
                nums[stackTop] = nums[i]
                stackTop += 1

        return stackTop
    