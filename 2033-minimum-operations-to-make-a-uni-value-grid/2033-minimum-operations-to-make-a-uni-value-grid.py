class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flatList = [num for row in grid for num in row]
        rem = flatList[0] % x
        for num in flatList:
            if num % x != rem:
                return -1
        #GET A MEDIAN
        flatList.sort()
        median = flatList[len(flatList)//2]

        res = 0
        for num in flatList:
            res += abs(num - median) // x

        return res
    
        
        # good but 34/60, mean based 
        # total = 0
        # n=len(grid)
        # m=len(grid[0])
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         total+=grid[r][c]
        # # print(total)
        # equi = total//(m*n)
        # # print(equi)
        # flatList = [item for sublist in grid for item in sublist]
        # nearestVal = min(flatList, key=lambda x: abs(x - equi))
        # # print(nearest_val)
        # res=0
        # for n in flatList:
        #     if n==nearestVal:
        #         continue
        #     elif n>nearestVal and n%x==0:
        #         res+= (n-nearestVal)//x 
        #     elif n<nearestVal and n%x==0:
        #         res += (nearestVal-n)//x
        #     elif n%x!=0:
        #         return -1
            
        
        # return res 