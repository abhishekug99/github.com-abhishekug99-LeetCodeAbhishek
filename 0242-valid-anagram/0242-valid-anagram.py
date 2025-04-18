class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Optimal
        if len(s)!=len(t):
            return False
        cntS = Counter(s)
        cntT = Counter(t)
        # print(cntS)
        for k, v in cntS.items():
            if k not in cntT.keys():
                return False
            if v!=cntT[k]:
                return False
        return True


        #BruteForce O(n)
        # res=[]
        # sList = list(s)
        # if len(s)!=len(t):
        #     return False
        # for char in t:
        #     if char in sList:
        #         sList.remove(char)
        #     else:
        #        return False
        # return True
        # return False    