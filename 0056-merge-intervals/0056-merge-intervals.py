class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return res
        intervals.sort(key=lambda x:x[0])
        res = []
        s,e = intervals[0]
        for i in range(1, len(intervals)):
            currS, currE  = intervals[i]
            
            if (e>=currS):
                e = max(e, currE)

            else:
                res.append([s,e])
                s, e = currS, currE

        res.append([s,e])
        return res