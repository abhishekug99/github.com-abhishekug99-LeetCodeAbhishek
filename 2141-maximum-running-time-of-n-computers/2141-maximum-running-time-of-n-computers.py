class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sumBatteries = sum(batteries)
        l, r = 1, sumBatteries//n

        while l<r:
            target = r - (r-l)//2       
            # print(target)
            extra = 0
            for power in batteries:
                extra+=min(power, target)
            # print(extra)
            if extra>=n*target:
                l = target
            else:
                r = target-1
        return l