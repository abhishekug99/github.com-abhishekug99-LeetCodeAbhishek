class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        left = costs[:candidates]
        right = costs[max(candidates, len(costs)-candidates):]
        # print((left,right))

        heapq.heapify(left)
        heapq.heapify(right)

        i, j = candidates, len(costs)-candidates-1

        for _ in range(k):
            if not right or (left and left[0]<=right[0]):
                res += heapq.heappop(left)
                # res+=wl
                if i<=j:
                    heapq.heappush(left, costs[i])
                    i+=1
            else:
                res += heapq.heappop(right)
                # res+=wr
                if i<=j:
                    heapq.heappush(right, costs[j])
                    j-=1
        return res
        
        
        # res = 0
        # # print(costs)
        # heapq.heapify(costs)
        # for _ in range(k):
        #     if len(costs)>=candidates:
        #         wc = heapq.heappop(costs)
        #         res+=wc 
        #         print(res)
        #     elif len(costs)<=candidates:
        #         res += min(costs)

        # return res
        