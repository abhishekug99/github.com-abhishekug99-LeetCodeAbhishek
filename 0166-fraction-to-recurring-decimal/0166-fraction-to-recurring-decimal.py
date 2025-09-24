class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator ==0:
            return "0"
        res = []

        if (numerator<0)^(denominator<0):
            res.append("-")
        
        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator//denominator))
        remainder  = numerator % denominator

        if remainder  ==0:
            return ''.join(res)
        
        res.append('.')
        seen = {}
        while remainder  !=0:
            print(seen)
            print(res)
            if remainder  in seen:
                res.insert(seen[remainder], "(")
                res.append(")")
                break
            seen[remainder ] = len(res)
            remainder *=10
            res.append(str(remainder//denominator))
            remainder %= denominator
        
        return "".join(res)

        # val = str(numerator/denominator)
        # valL = val.split('.')
        # if valL[0] == '0' and len(valL[1])==1:
        #     return val
        # if valL[1] == '0' and len(valL)==2:
        #     return valL[0]
        # res=''
        # decimal = ''
        # nonre = (valL[1])
        # print(nonre)
        # for d in nonre:
        #     decimal += d
        # res = val[0] + '.' +'(' + decimal +')'
        # return res
