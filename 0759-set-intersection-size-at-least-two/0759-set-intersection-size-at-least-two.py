class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1], -x[0]))
        print(intervals)
        res = 0
        a = b = -1

        for l,r in intervals:
            if b<l:
                res+=2
                a = r-1
                b=r
            elif a<l<=b:
                res+=1
                a=b
                b=r
        return res     

