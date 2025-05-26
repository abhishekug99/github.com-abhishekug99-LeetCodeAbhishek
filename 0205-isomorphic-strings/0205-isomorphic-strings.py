class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            
        def transform(string):
            iMap = {}
            result = []
            for i, ch in enumerate(string):
                if ch not in iMap:
                    iMap[ch] = i
                result.append(iMap[ch])
            return result

        return transform(s) == transform(t)
        
        # if len(s)!=len(t):
        #     return False
        # if s==t:
        #     return True
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         continue
        #     else:
        #         return False

        # cntS = Counter(s)
        # cntT = Counter(t)
        # print(cntS)
        # print(cntT)

        # if list(cntS.values()) == list(cntT.values()):
        #     return True
        
        
        # return False
        