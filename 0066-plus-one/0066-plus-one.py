class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sumn=0
        final =[]
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digi = ''.join(digits)
        res = int(digi) + 1
        res = str(res)
        for d in res:
            final.append(int(d))
        return final    
