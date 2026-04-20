class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
    
        res = 0
        
        for j in range(n - 1, -1, -1):
            if colors[j] != colors[0]:
                res = j
                break
        
        for i in range(n):
            if colors[i] != colors[-1]:
                res = max(res, n - 1 - i)
                break
        
        return res
        # minHeap = []
        # maxHeap = []
        # res = 0
        # for i,c in enumerate(colors):
        #     heapq.heappush(minHeap,(c,i))
        #     heapq.heappush(maxHeap,(-c,i))
        
        # while minHeap and maxHeap:
        #     minc,minI = heapq.heappop(minHeap)
        #     maxc,maxI = heapq.heappop(maxHeap)
        #     if (-maxc) != minc:
        #         res = max(res, abs(minI-maxI))
        
        # return res