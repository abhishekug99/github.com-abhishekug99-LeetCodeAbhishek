class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # linear time
        right_sum = sum(nums)
        left_sum = 0
        res = []

        for num in nums:
            right_sum -= num
            res.append(abs(left_sum - right_sum))
            left_sum += num
        return res

        #worked and accepted
        # res = [0]*len(nums)
        # for i in range(len(nums)):
        #     if i==0:
        #         res[i] = sum(nums[i+1:])
        #     elif i==len(nums)-1:
        #         res[i] = sum(nums[:i])
        #     else:
        #         res[i] = abs(sum(nums[i+1:])-sum(nums[:i]))
        
        # return res