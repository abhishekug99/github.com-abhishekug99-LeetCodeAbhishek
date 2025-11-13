import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O(n)
        def quickselect(left, right, idx_to_find):
            pivot = nums[random.randint(left, right)]
            l, r = left, right
            
            while l <= r:
                while nums[l] > pivot:
                    l += 1
                while nums[r] < pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
            
            if idx_to_find <= r:
                return quickselect(left, r, idx_to_find)
            elif idx_to_find >= l:
                return quickselect(l, right, idx_to_find)
            else:
                return nums[idx_to_find]

        # kth largest → index k-1 in descending order
        return quickselect(0, len(nums) - 1, k - 1)

