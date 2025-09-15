class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        if s==t:
            return s
        cntT, window = {}, {}

        for c in t:
            cntT[c] = 1+cntT.get(c,0)
        
        have, need = 0, len(cntT)
        res, resLen = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)

            if c in cntT and  window[c] == cntT[c]:
                have+=1
            
            while have==need:
                #update res
                if (r-l+1)<resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                #pop from left of or window
                window[s[l]] -=1
                if s[l] in cntT and window[s[l]]<cntT[s[l]]:
                    have-=1
                l+=1
        
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""


        
        # Bruteforce and correct O(n^2)
        # if len(t)>len(s):
        #     return ""
        # if s==t:
        #     return s
        
        # minWindow = len(t)+1
        # i=0
        # res=''
        # while i<len(s):
        #     if s[i] in t:
        #         tMap=Counter(t)
        #         j=i
        #         tmpStr=''
        #         while j<len(s):
        #             tmpStr+=s[j]
        #             if s[j] in tMap:
        #                 if tMap[s[j]]>1:
        #                     tMap[s[j]] -=1
        #                 else:
        #                     del tMap[s[j]]
        #             if not tMap:
        #                 if not res or len(tmpStr)<len(res):
        #                     res = tmpStr
        #                 break
        #             j+=1
        #     i+=1

        # return res 

