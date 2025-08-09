import heapq
class MedianFinder:

    def __init__(self):
        self.arr = []
        # heapq.heapify(self.arr)

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)   

    def findMedian(self) -> float:
        median = 0
        if len(self.arr)%2 == 0:
            idx = (len(self.arr)-1)//2
            median = (self.arr[idx] + self.arr[idx+1])/2
        elif len(self.arr)%2 != 0:
            idx =(len(self.arr))//2
            median = self.arr[idx]
        return median
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()