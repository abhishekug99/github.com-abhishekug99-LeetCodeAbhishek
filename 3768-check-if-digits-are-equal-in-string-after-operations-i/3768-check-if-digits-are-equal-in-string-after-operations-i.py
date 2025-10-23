class Solution:
    def hasSameDigits(self, s: str) -> bool:
        i=0
        n = len(s)

        
        while len(s)>2:
            tmp=''
            for j in range(len(s)-1):
                # print(str((int(s[j])+ int(s[j+1]))% 10))
                tmp+= str((int(s[j])+ int(s[j+1]))% 10) 
            s = tmp
            
        print(s)
        return len(s) == 2 and s[0]==s[1]
