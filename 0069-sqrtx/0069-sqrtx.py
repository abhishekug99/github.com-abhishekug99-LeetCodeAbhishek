class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l,h = 1,x
        while l<=h:
            mid  = l+(h-l)//2
            if mid * mid == x:
                return mid
            elif (mid*mid) < x:
                l = mid+1
            # elif (mid*mid)>x:
            else:
                h = mid - 1
            
            
        return h
