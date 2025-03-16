class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j =0, len(heights)-1
        volume = 0
        while i!=j:
            if heights[i]<=heights[j]:
                volume = max(heights[i]*(j-i), volume)
                i=i+1
            else:
                volume = max(heights[j]*(j-i), volume)
                j-=1

        
        return volume
