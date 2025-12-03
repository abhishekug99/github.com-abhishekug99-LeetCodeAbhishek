class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        cnt1 = defaultdict(lambda: defaultdict(int))
        cnt2 = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)
                if g < 0:
                    g = -g
                if g != 0:
                    dx0 = dx // g
                    dy0 = dy // g
                else:
                    dx0 = dy0 = 0

                if dx0 < 0 or (dx0 == 0 and dy0 < 0):
                    dx0 = -dx0
                    dy0 = -dy0

                slope = (dy0, dx0)

                a = dy
                b = -dx
                c = a * x1 + b * y1   # we can use ax + by = c form

                g2 = gcd(gcd(abs(a), abs(b)), abs(c))
                if g2 != 0:
                    a //= g2
                    b //= g2
                    c //= g2

                if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
                    a = -a
                    b = -b
                    c = -c

                line_id = (a, b, c)

                cnt1[slope][line_id] += 1

                mid_key = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
                cnt2[mid_key][slope] += 1

        ans = 0
        for lines in cnt1.values():
            s = 0
            for t in lines.values():
                ans += s * t
                s += t

        for slopes in cnt2.values():
            s = 0
            for t in slopes.values():
                ans -= s * t
                s += t

        return ans


        #My approach works well only one test case miss O(n^2) O(n^2) time and space
        # MOD = 10**9 + 7
        # n = len(points)

        # slopeToLines = defaultdict(lambda: defaultdict(set))

        # for i in range(n):
        #     x1, y1 = points[i]
        #     for j in range(i+1,n):
        #         x2,y2 = points[j]

        #         dx = x2-x1
        #         dy = y2-y1
        #         #normalising slope (dy/g, dx/g)
        #         g = gcd(dx, dy)
        #         dx0 = dx//g
        #         dy0 = dy//g
        #         #normalise sign
        #         if dx0<0 or (dx0==0 and dy0<0):
        #             dx0 = -dx0
        #             dy0 = -dy0
                
        #         slope = (dy0, dx0)
        #         #normalise line ax+by+c =0 normal vector (a,b)=(dy, -dx)
                
        #         a = dy
        #         b = -dx
        #         c = -(a*x1+b*y1)

        #         g2 = gcd(gcd(abs(a), abs(b)), abs(c))
        #         if g2!=0:
        #             a//=g2
        #             b//=g2
        #             c//=g2
                
        #         #unify line to easy to know line is unique
        #         if a<0 or (a==0 and b<0) or (a==0 and b==0 and c<0):
        #             a=-a
        #             b=-b
        #             c=-c
        #         line = (a,b,c)
        #         slopeToLines[slope][line].add(i)
        #         slopeToLines[slope][line].add(j)

        # #counting phase
        # res = 0
        # for slope, lineDict in slopeToLines.items():
        #     counts = []

        #     for pts in lineDict.values():
        #         p = len(pts)
        #         if p >= 2:
        #             counts.append(p*(p-1)//2)

        #     if len(counts) < 2:
        #         continue

        #     S = sum(counts)
        #     SS = sum(c*c for c in counts)

        #     res += (S*S - SS) // 2
        #     res %= MOD

        # return res



