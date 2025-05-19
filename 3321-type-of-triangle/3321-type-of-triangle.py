class Solution:
    def triangleType(self, nums: List[int]) -> str:
        tri = set()
        if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[0]+nums[2]>nums[1]:
            for num in nums:
                tri.add(num)
            if len(tri) == 1:
                return "equilateral"
            if len(tri) == 2:
                return "isosceles"
            else: return "scalene"
        else:
            return "none"