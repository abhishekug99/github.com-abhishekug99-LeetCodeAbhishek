# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))
        # l,h = 1,n
        # while l<h:
        #     m = (l+h)//2
        #     if guess(m) == 1:
        #         l = m+1
        #     else:
        #         h = m
        # return l

