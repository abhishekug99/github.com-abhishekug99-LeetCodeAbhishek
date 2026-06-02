class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        for ls, ld in zip(landStartTime, landDuration):
            landFinish = ls+ld
            for ws, wd in zip(waterStartTime, waterDuration):
                finish1 = max(ws, landFinish) + wd
                finish2 = max(ls, ws+wd) + ld

                res = min(res, finish1,finish2)

        return res 