class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue

            cnt = defaultdict(int)
            for b_val in sti:
                cnt[b_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans

        #My approach works well only one test case miss O(n^2) O(n^2) time and space
        MOD = 10**9 + 7
        n = len(points)

        slopeToLines = defaultdict(lambda: defaultdict(set))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]

                dx = x2-x1
                dy = y2-y1
                #normalising slope (dy/g, dx/g)
                g = gcd(dx, dy)
                dx0 = dx//g
                dy0 = dy//g
                #normalise sign
                if dx0<0 or (dx0==0 and dy0<0):
                    dx0 = -dx0
                    dy0 = -dy0
                
                slope = (dy0, dx0)
                #normalise line ax+by+c =0 normal vector (a,b)=(dy, -dx)
                
                a = dy
                b = -dx
                c = -(a*x1+b*y1)

                g2 = gcd(gcd(abs(a), abs(b)), abs(c))
                if g2!=0:
                    a//=g2
                    b//=g2
                    c//=g2
                
                #unify line to easy to know line is unique
                if a<0 or (a==0 and b<0) or (a==0 and b==0 and c<0):
                    a=-a
                    b=-b
                    c=-c
                line = (a,b,c)
                slopeToLines[slope][line].add(i)
                slopeToLines[slope][line].add(j)

        #counting phase
        res = 0
        for slope, lineDict in slopeToLines.items():
            counts = []

            for pts in lineDict.values():
                p = len(pts)
                if p >= 2:
                    counts.append(p*(p-1)//2)

            if len(counts) < 2:
                continue

            S = sum(counts)
            SS = sum(c*c for c in counts)

            res += (S*S - SS) // 2
            res %= MOD

        return res



