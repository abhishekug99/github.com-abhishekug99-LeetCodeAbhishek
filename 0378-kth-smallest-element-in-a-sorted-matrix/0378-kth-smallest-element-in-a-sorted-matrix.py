class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) ==1 and len(matrix[0])==1:
            return matrix[0][0]
        
        full = []
        for i in range(len(matrix)):
            full+=matrix[i]
        heapq.heapify(full)
        j=0
        while j<k:
            res = heapq.heappop(full)
            j+=1
        
        return res
        