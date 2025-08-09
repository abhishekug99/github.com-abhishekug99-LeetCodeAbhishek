import heapq
class MedianFinder:
# nlog(n) as bisect.insort uses binary search apperoch to find insertion point #easy to implement
    # def __init__(self): 
    #     self.arr = []
    #     # heapq.heapify(self.arr)

    # def addNum(self, num: int) -> None:
    #     bisect.insort(self.arr, num)   

    # def findMedian(self) -> float:
    #     median = 0
    #     if len(self.arr)%2 == 0:
    #         idx = (len(self.arr)-1)//2
    #         median = (self.arr[idx] + self.arr[idx+1])/2
    #     elif len(self.arr)%2 != 0:
    #         idx =(len(self.arr))//2
    #         median = self.arr[idx]
    #     return median
 
# Heap based min max both heaps #O(log(n)) as heap does operations, push/pop in log(n) time
# more optimised
    def __init__(self):
        self.small = [] #maxHeap
        self.large = [] #minHeap
        # heapq.heapify(self.arr)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num) #add max heap

        if self.small and self.large and (-self.small[0]>self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        #balance size
        if len(self.small)>len(self.large) +1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large)>len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))



    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()