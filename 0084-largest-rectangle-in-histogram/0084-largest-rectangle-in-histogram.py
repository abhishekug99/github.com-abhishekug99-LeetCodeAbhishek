class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1] -1 
                maxArea = max(maxArea, height*width)
            stack.append(i)
        return maxArea
        
        #correct but bruteforce and bugs in handlinh 0 height
        # if len(heights) ==2 and min(heights)!=0:
        #     return min(heights)*2
        # if len(heights) ==2 and min(heights)==0:
        #     return max(heights)
        # if len(heights) == 1:
        #     return heights[0]

        # n = len(heights)
        # maxArea = 0
        # for i in range(0, n):
        #     tmp=[]
        #     j=i+1
        #     area = 0
        #     while j<n:
        #         if heights[j-1]<=heights[j] and (heights[j]!=0 and heights[j-1]!=0 ):
        #             tmp.append(heights[j-1])
        #             tmp.append(heights[j])
        #             # print(tmp)
        #         elif heights[j-1]>heights[j]:
        #         # else:
        #             break
        #         j+=1
        #     if tmp:
        #         area = min(tmp) * len(tmp)
        #     maxArea = max(area,maxArea)
        
        # return maxArea
        