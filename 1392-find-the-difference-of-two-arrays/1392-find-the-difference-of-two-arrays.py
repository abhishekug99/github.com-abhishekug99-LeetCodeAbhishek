class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #More Optimised using frozen set
        frozenSetNums1 = set(nums1)
        frozenSetNums2 = set(nums2)

        diff1 = list(frozenSetNums1-frozenSetNums2)
        diff2 = list(frozenSetNums2-frozenSetNums1)
        
        return [diff1,diff2]

        
        #beats 13.98
        # num1Filter = set()
        # num2Filter = set()
        # res = []
        # for num in nums1:
        #     if num not in nums2:
        #         num1Filter.add(num)
        # res.append(list(num1Filter))
        # for num in nums2:
        #     if num not in nums1:
        #         num2Filter.add(num)
        # res.append(list(num2Filter))
        # return res
