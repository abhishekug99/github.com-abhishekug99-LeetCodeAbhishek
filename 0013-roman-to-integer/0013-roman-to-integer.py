class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and romanMap[s[i]] <romanMap[s[i+1]]:
                res-=romanMap[s[i]]
            else:
                res+=romanMap[s[i]]
        return res
        
        # def get_next(num):
        #     total = 0
        #     while num > 0:
        #         digit = num % 10
        #         total += digit * digit
        #         num //= 10
        #     return total

        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     n = get_next(n)
        # return n == 1
