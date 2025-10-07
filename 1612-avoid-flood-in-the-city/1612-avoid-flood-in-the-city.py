import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1]*n
        dry_days = []
        lastRain = {}

        for i, lake in enumerate(rains):
            if lake>0: 
               
                if lake in lastRain:
                    idx = bisect.bisect_right(dry_days, lastRain[lake])
                    if idx == len(dry_days):
                        return []
                    dryIdx = dry_days.pop(idx)
                    res[dryIdx] = lake
                    # dry_days.pop(idx)
                    # full.remove(lake)

               
                lastRain[lake]=i

            else:
                bisect.insort(dry_days, i)
                res[i] = 1
        return res


        
        # stack = []
        # res = [-1]*len(rains)
        # for i in range(len(rains)):
        #     if rains[i]>1:
        #         stack.append(rains[i])
        #     elif rains[i]==0 and stack:
        #         res[i] = stack.pop()
        # return res