class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            s=intervals[i][0]
            e=intervals[i][1]
            if newInterval[1] < s:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0] > e:
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0], s), max(newInterval[1], e)]
                #this could be overlapping so we wont add it right now
        
        res.append(newInterval)
            
        return res
        