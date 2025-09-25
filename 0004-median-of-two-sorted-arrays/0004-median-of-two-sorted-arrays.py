import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            idx = bisect.bisect_left(nums1, num)
            nums1.insert(idx, num)
        print(nums1[-1]+nums1[0])
        
        if len(nums1) %2 != 0:
            return nums1[len(nums1)//2]
        
        res  = (nums1[len(nums1)//2] +  nums1[(len(nums1)//2)-1])/2
        return res

        