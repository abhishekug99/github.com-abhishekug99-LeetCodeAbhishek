class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1,n2) for n1, n2 in zip(nums1,nums2)]
        # print(pairs)
        pairs = sorted(pairs,key=lambda p:p[1], reverse = True) #sort based on nums2 in decending order
        print(pairs)
        minHeap = []
        num1Sum = 0
        res = 0
       
        for n1, n2 in pairs:
            num1Sum+=n1
            heapq.heappush(minHeap,n1)

            if len(minHeap)>k:
                n1Pop = heapq.heappop(minHeap)
                num1Sum -= n1Pop
            
            if len(minHeap) == k:
                res = max(res,num1Sum*n2)
        return res
        