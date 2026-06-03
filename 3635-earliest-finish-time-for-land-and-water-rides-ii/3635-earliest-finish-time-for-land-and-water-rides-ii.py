from typing import List
from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],waterDuration: List[int]) -> int:

        # land ride first
        minEnd = 10**10
        for s, d in zip(landStartTime, landDuration):
            minEnd = min(minEnd, s+d)
        
        ans = 10**10
        for s, d in zip(waterStartTime, waterDuration):
            ans = min(ans, d + max(minEnd, s))
        
        # water ride first
        minEnd = 10**10
        for s, d in zip(waterStartTime, waterDuration):
            minEnd = min(minEnd, s+d)
        
        for s, d in zip(landStartTime, landDuration):
            ans = min(ans, d + max(minEnd, s))
        
        return ans