class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        best = 0
        res = 0

        for s, e, v in events:
            while heap and heap[0][0]<s:
                end, val = heapq.heappop(heap)
                best = max(best, val)

            res = max(res, best+v)
            heapq.heappush(heap,(e,v))
        return res

        # bruteforce
        # events.sort(key=lambda x:x[0])
        # # print(events)
        # res = 0
        # for i in range(len(events)):
        #     s,e,v = events[i]
        #     res = max(res, v)
        #     j=i+1
        #     for j in range(i+1, len(events)):
        #         if e<events[j][0]:
        #             res = max(res, v+events[j][2])
        #             break
        #     # res = max(currVal, res)
        # return res
                
