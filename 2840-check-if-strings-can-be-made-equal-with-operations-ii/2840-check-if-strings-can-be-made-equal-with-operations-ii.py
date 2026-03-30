class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1odd,s1even = [], []
        s2odd,s2even = [], []
        
        for i in range(len(s1)):
            if i%2==0:
                s1even.append(s1[i])
                s2even.append(s2[i])
            else:
                s1odd.append(s1[i])
                s2odd.append(s2[i])   
        
        return True if (sorted(s1odd)==sorted(s2odd) and sorted(s1even)==sorted(s2even)) else False 