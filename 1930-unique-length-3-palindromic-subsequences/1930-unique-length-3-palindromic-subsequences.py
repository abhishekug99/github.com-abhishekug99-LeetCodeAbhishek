class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        for m in s:
            right[m] -= 1
            for c in left:
                if right[c]>0:
                    res.add((m,c))
            left.add(m)
        return len(res)
        
        # O(n^2) TLE
        # known = set()
        # if len(s)<=3 and s!=s[::-1]:
        #     return 0
        # elif len(s)==3 and s==s[::-1]:
        #     return 1
        
        # for ch in s:
        #     l  = s.find(ch)
        #     r  = s.rfind(ch)
        #     if r-l>1:
        #         for i in range(l+1,r):
        #             known.add(s[l]+s[i]+s[r])
        # return len(known) 

        # return len(res)
