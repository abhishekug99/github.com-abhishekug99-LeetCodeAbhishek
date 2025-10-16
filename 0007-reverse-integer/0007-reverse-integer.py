class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
    
        if x>0:
            xs = str(x)
            xs = xs[::-1]
            return int(xs) if int(xs) < (2**31 - 1) else 0

        if x<0:
            xs = str(x)
            xs = xs[1:]
            xs = xs[::-1]
            return -int(xs) if -int(xs) > (-2**31) else 0

