class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        Y = 0
        totalArea = 0
        for x,y,l in squares:
            totalArea += l**2
            Y = max(Y, y+l)

        def isYGood(tempY):
            area = 0
            for x,y,l in squares:
                if y < tempY:
                    area += l * min(tempY-y, l)
            return area >= totalArea/2

        l,h = 0, Y
        eps = 1e-5
        while abs(h-l)>eps:
            mid = (h+l)/2
            if isYGood(mid):
                h = mid
            else:
                l=mid
        return h  