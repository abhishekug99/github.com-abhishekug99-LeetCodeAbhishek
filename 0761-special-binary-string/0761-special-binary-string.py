class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        special = []
        start=0
        sumb = 0

        for i in range(len(s)):
            if s[i]=='1':
                sumb+=1
            else:
                sumb-=1
            
            if sumb==0:
                inner = s[start+1:i]
                special.append('1'+self.makeLargestSpecial(inner)+'0')
                start = i+1
                print(special)
        
        special.sort(reverse=True)
        return "".join(special)
