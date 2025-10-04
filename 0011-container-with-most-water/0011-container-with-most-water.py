class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j =0, len(height)-1
        volume = 0
        while i!=j:
            if height[i]<=height[j]:
                volume = max(height[i]*(j-i), volume)
                i=i+1
            else:
                volume = max(height[j]*(j-i), volume)
                j-=1

        
        return volume