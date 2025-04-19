import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.nums = []
        self.numSet = set()
        heapq.heapify(self.nums)

    def popSmallest(self) -> int:
        if self.nums:
            smallest = heapq.heappop(self.nums)
            self.numSet.remove(smallest)
            return smallest
        else:
            self.curr+=1
            return self.curr-1

    def addBack(self, num: int) -> None:
        if num>0 and num < self.curr and num not in self.numSet:
            heapq.heappush(self.nums,num)
            self.numSet.add(num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)