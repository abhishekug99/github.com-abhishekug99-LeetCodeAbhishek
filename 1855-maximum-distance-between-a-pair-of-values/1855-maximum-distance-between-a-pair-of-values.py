class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        res = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1

        return res
        
        #works well bbruteforce (n*m)
        # res= 0
        # for j in range(len(nums2)):
        #     if j+1>=len(nums1):
        #         for i in range(0, len(nums1)):
        #             if nums1[i] <= nums2 [j]:
        #                 res = max(res, abs(j-i))
        #     else:    
        #         for i in range(0, j+1):
        #             if nums1[i] <= nums2 [j]:
        #                 res = max(res, abs(j-i))
        
        # return res