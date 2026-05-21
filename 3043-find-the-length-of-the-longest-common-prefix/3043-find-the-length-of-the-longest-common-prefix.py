class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            s = str(num)
            prefix = ""
            for ch in s:
                prefix += ch
                prefixes.add(prefix)

        res = 0

        # Check prefixes in arr2
        for num in arr2:
            s = str(num)
            prefix = ""
            for ch in s:
                prefix += ch
                if prefix in prefixes:
                    res = max(res, len(prefix))

        return res
        
        
        # res = 0
        # for n1 in arr1:
        #     n1s = str(n1)
        #     for n2 in arr2:
        #         n2s = str(n2)
        #         if n1s[0]!=n2s[0]:
        #             continue
        #         i=0
        #         cnt = 0
        #         while i < min(len(n1s), len(n2s)):
        #             if n1s[i]==n2s[i]:
        #                 cnt+=1
        #             else:
        #                 break
        #             i+=1
        #         res = max(res, cnt)
        # return res
