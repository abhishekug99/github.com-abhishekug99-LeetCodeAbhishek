class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = list(zip(capital,profits))
        capitalMinHeap = []
        maxProfitheap = []
        # print(projects)
        for c,p in projects:
            heapq.heappush(capitalMinHeap, (c,p))
        
        for _ in range(k):
            while capitalMinHeap and capitalMinHeap[0][0]<=w:
                c,p = heapq.heappop(capitalMinHeap)
                heapq.heappush(maxProfitheap, -p)
                # print(maxProfitheap)
            if not maxProfitheap:
                break
            w+= (-heapq.heappop(maxProfitheap))
        return w

        # res = []
        # heapq.heapify(profits)
        # heapq.heapify(capital)
        # for i in range(len(profits)):
        #     tmpC = heapq.heappop(capital)
        #     tmpP  = heapq.heappop(profits)
        #     if tmpC>=w and len(res)<k:
        #         res.append(tmpP)
        #     if len(res) == k and res[-1] < tmpP:
        #         res[-1] = tmpP
        # return sum(res)


        