class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=[]
        sList = list(s)
        if len(s)!=len(t):
            return False
        for char in t:
            if char in sList:
                sList.remove(char)
            else:
               return False
        return True
        # return False    