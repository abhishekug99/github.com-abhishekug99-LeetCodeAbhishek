class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        
        side = 0

        for i in range(n):
            for j in range(i+1,n):
                topRX = min(topRight[i][0], topRight[j][0])
                bottomLX = max(bottomLeft[i][0], bottomLeft[j][0])

                w = topRX-bottomLX

                topRY = min(topRight[i][1], topRight[j][1])
                bottomLY = max(bottomLeft[i][1], bottomLeft[j][1])

                h = topRY - bottomLY
                currside = min(w,h)

                side = max(side, currside)

        return side**2 