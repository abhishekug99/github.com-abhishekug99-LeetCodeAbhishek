class Solution:
    def partitionString(self, s: str) -> int:
        i=0
        
        subSList = []
        while i< len(s):
            subS = s[i]
            j=i+1
            while j<len(s):
                if s[j] not in  subS:
                    subS += s[j]
                else:
                    break
                j+=1
            subSList.append(subS)
            i=j   
        print(subSList)
        return len(subSList)
