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
        
        
        # pos = defaultdict(lambda: [float('inf'), -1])
    
        # # Step 1: record min and max index per color
        # for i, c in enumerate(colors):
        #     pos[c][0] = min(pos[c][0], i)
        #     pos[c][1] = max(pos[c][1], i)
        
        # # Step 2: build heaps by index
        # minHeap = []
        # maxHeap = []
        
        # for c, (mn, mx) in pos.items():
        #     heapq.heappush(minHeap, (mn, c))
        #     heapq.heappush(maxHeap, (-mx, c))
        
        # res = 0
        
        # # Step 3: for each color, compare with global extremes
        # for c, (mn, mx) in pos.items():
            
        #     # Get smallest index of a different color
        #     while minHeap and minHeap[0][1] == c:
        #         heapq.heappop(minHeap)
        #     if minHeap:
        #         res = max(res, abs(mx - minHeap[0][0]))
            
        #     # Get largest index of a different color
        #     while maxHeap and maxHeap[0][1] == c:
        #         heapq.heappop(maxHeap)
        #     if maxHeap:
        #         res = max(res, abs(mn - (-maxHeap[0][0])))
        
        # return res