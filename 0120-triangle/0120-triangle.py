class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        return triangle[0][0]
        
        # if len(triangle) == 1:
        #     return min(triangle[0])
        # sumMin = 0
        # j=0
        # for i in range(len(triangle)):
        #     if i == 0:
        #         sumMin+=min(triangle[j])
        #     else:
        #         sumMin+=min(triangle[j:])
        #         j+=1
        
        # return sumMin