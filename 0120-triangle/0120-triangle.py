import heapq
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1] )
        return triangle[0][0]

        # res = triangle[0][0]
        # idx  = 0
        # minVal=0
        # for i in range(1, len(triangle)): 
        #     for j in range(len(triangle[i])):
        #         if i == 1:
        #             minVal = min(triangle[i])
        #             res+=minVal
        #             idx = triangle[i].index(minVal)
        #         else:
        #             minVal = min(triangle[i][idx], triangle[i][idx+1])
        #             res+=minVal
        #             idx = triangle[i].index(minVal)
        # return res

        