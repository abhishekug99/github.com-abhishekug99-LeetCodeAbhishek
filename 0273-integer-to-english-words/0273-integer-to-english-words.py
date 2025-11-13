class Solution:
    def numberToWords(self, num: int) -> str:
        if num ==0:
            return 'Zero'
        zero = {0: "Zero"}
        onesMap = {
        19: "Nineteen", 18: "Eighteen", 17: "Seventeen",
        16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen",
        12: "Twelve", 11: "Eleven", 10: "Ten", 9: "Nine", 8: "Eight",
        7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three",
        2: "Two", 1: "One"}
        
        tensMap = {90: "Ninety", 80: "Eighty", 70: "Seventy",
        60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty",
        20: "Twenty"}

        def getStr(n): #n would be of three digits
            res = []
            hundreds = n//100
            if hundreds:
                res.append(onesMap[hundreds] + " Hundred")
            last2 = n % 100
            if last2>=20:
                tens, ones = last2//10, last2%10
                res.append(tensMap[tens*10])
                if ones:
                    res.append(onesMap[ones])

            elif last2:
                res.append(onesMap[last2])


            return " ".join(res)
        
        postfix = ["", " Thousand", " Million", " Billion"]
        i=0
        res = []
        while num:
            digits = num%1000

            s = getStr(digits)
            if s:
                res.append(s + postfix[i])
            num = num//1000
            i+=1
        res.reverse()
        return " ".join(res)