class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        for i in range(min(k,len(nums1))):
            heapq.heappush(heap,(nums1[i]+nums2[0], i, 0))
        # print(heap)
        while heap and len(res)<k:
            curSum,i,j = heapq.heappop(heap)
            res.append([nums1[i],nums2[j]])
        
            if j+1<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1], i, j+1))
        return res


        # works well time (nlogn) need to be improved
        # comb = list(itertools.product(nums1, nums2)) # this is taking lot of time
        # heap = []
        # for p,q in comb:
        #     heapq.heappush(heap, (p+q,[p,q]))
        
        # res = []
        # for _ in range(min(k,len(heap))):
        #     res.append(heapq.heappop(heap)[1])
        # # heapq.heapify(comb)
        
        # return res


        