class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        negCnt = 0
        minAbs = float('inf')
        for r in matrix:
            for val in r:
                res+=abs(val)
                if val<0:
                    negCnt+=1
                minAbs = min(minAbs, abs(val))
        if negCnt%2==1:
            res-= 2*minAbs
        
        return res
        
        # partially correct
        # n = len(matrix)
        # def getSum(matrix):
        #     totalSum = 0
        #     for i in range(len(matrix)):
        #         totalSum+=sum(matrix[i])
        #     return totalSum
        
        # initialSum = getSum(matrix)
        # res = float('-inf')
        # nbrs = [(1,0), (-1,0), (0,1), (0,-1)]
        # copyMatrix = copy.deepcopy(matrix)
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         currSum = 0
        #         for dr,dc in nbrs:
        #             nr,nc = r+dr, c+dc
        #             if nr<0 or nc<0 or nr>=n or nc>=n:
        #                 continue
        #             elif matrix[nr][nc]<0:
        #                 matrix[nr][nc] = (matrix[nr][nc])*-1
        #                 matrix[r][c] = (matrix[r][c])*-1
        #                 currSum = getSum(matrix)
        #                 if currSum>initialSum or currSum>res:
        #                     res = max(res, currSum, initialSum)
        #                 else:
        #                     matrix[nr][nc] = (matrix[nr][nc])*-1
        #                     matrix[r][c] = (matrix[r][c])*-1                
        #                 print(res)
        # if copyMatrix == matrix:
        #     return getSum(matrix)
        # return res

                

