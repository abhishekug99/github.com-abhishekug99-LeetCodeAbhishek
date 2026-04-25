class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        P=4*side
        pos = []
        for x,y in points:
            if y==0:
                pos.append(x)
            elif x==side:
                pos.append(side+y)
            elif y==side:
                pos.append(3*side-x)
            else:
                pos.append(4*side-y)
        pos.sort()
        n=len(pos)

        pos2 = pos + [p+P for p in pos]

        def can(d):
            for start in range(n):
                cnt=1
                last=pos2[start]
                for i in range(start+1, start+n):
                    if pos2[i]-last>=d:
                        cnt+=1
                        last=pos2[i]
                        if cnt==k:
                            if P-(last-pos2[start])>=d:
                                return True
                            break
                if cnt<k:
                    break
            return False
        lo,hi=0,P
        while lo<=hi:
            mid = (lo+hi)//2
            if can(mid):
                lo=mid+1
            else:
                hi=mid-1
        return hi