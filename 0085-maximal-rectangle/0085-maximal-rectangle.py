class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestInHistogram(histo):
            stack = []
            maxArea = 0
            histo.append(0)
            for i, h in enumerate(histo):
                while stack and histo[stack[-1]]>h:
                    height = histo[stack.pop()]
                    width = i if not stack else i-stack[-1] -1 
                    maxArea = max(maxArea, height*width)
                stack.append(i)
            return maxArea
        
        n = len(matrix)
        m = len(matrix[0])
        stack = [0]*n
        dp = [[0]*m for _ in range(n)]
        # print(dp)
        for j in range(m):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j]=='1':
                    if dp[i-1][j]!='0' or matrix[i-1][j]!=0:
                        dp[i][j] += int(dp[i-1][j]) + int(matrix[i][j]) 
                elif matrix[i][j]=='0':
                    dp[i][j]=0

        for r in range(n):
            stack[r] = largestInHistogram(dp[r])
        
        return max(stack)




        
