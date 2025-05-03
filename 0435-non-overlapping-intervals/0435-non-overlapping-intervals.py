class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt+=1
            else:
                end = intervals[i][1]
        return cnt

            # if intervals[i][1]>intervals[i+1][0] or intervals[i][0] == intervals[i+1][0] or intervals[i][0] == intervals[i][1]:
                # cnt+=1

        # return cnt   
        # stack1 = []
        # stack2 = []
        # for i in range(len(intervals)):
        #    if intervals[i][0] in stack1:
        #     stack1.pop()
        #     cnt+=1
        #    stack1.append(intervals[i][0])
           
        # return cnt
        
            
            




