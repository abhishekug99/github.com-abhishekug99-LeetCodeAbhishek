from itertools import combinations
import math
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visted = set()
        res=[]
        def backtrackDFS(start: int, path: List):
            if len(path) == k:
                res.append(path[:]) #stores the copy of path
                return
            for i in range(start, n+1):
                path.append(i)
                backtrackDFS(i+1, path)
                path.pop()
        
        backtrackDFS(1, [])
        return res

        
        # visited = set()
        # lenComb = int(math.factorial(n)/(math.factorial(k) * math.factorial(n-k)))
        # i=0
        # res = []
        # def backtrackDFS(r, c, lenComb):
        #     if len(res) == lenComb:
        #         return res
        #     if r>lenComb or c > k:
        #         return 
        #     if (r,c) or (c,r) not in visited:
        #         res.append([r,c])
        #         visited.add((r,c))
                
        #     backtrackDFS(r, c+1, lenComb)
        #     backtrackDFS(r+1, c, lenComb)

        #     visited.remove((r,c))

        # return backtrackDFS(1, 1, lenComb)

        