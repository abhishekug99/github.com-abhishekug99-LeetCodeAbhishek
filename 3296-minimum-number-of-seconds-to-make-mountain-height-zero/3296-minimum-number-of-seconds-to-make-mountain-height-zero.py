class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def canFinish(T):
            total = 0
            for t in workerTimes:
                x = int((math.sqrt(1 + 8*T/t) - 1) // 2)
                total += x
            return total >= mountainHeight
        
        l, r = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while l < r:
            mid = (l + r) // 2
            if canFinish(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        