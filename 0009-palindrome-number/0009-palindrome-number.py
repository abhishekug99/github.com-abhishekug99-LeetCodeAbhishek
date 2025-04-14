class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0<=x<10:
            return True
        if 0>=x>-10:
            return False
        is_negative = x < 0
        x = abs(x)
        digits = []
        while x > 0:
            digits.insert(0, x % 10)
            x //= 10
        if is_negative:
            digits[0] *= -1  
    
        if digits == digits[::-1]:
            return True
        else: return False
