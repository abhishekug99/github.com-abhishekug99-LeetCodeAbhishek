class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        strL = list(map(str, digits))
        num = int(''.join(strL))
        num+=1
        res = map(int, str(num)) 
        return [int(x) for x in str(num)]





        # if lastInt < 9:
        #     lastInt = int(strL.pop())
        #     lastInt+=1
        #     strL.append(str(lastInt))
        #     nDigits = list(map(int, strL))
        #     return nDigits
            
        # if lastInt == 9 and len(digits)>1:
        #     strL.pop()
        #     strL.append('1')
        #     strL.append('0')
        #     nDigits = list(map(int, strL))
        #     return nDigits

        # if lastInt == 9 and len(digits)==1:
        #     newLst = []
        #     newLst.append(1)
        #     newLst.append(0)
        #     return newLst

        # if lastInt < 9 and len(digits)==1:
        #     newLst = []
        #     last = digits[0]
        #     newLst.append(last+1)
        #     return newLst
        




        