class Solution:
    def smallestNumber(self, n: int) -> int:
        num = n
        while num>=n:
            # biNum = bin
            if '0' in (bin(num)[2:]):
                num+=1
            else:
                return num
                break