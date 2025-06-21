class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        stack = []
        j  = 0
        if not s:
            return True
        if not t:
            return False
            
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                stack.append(t[i])
                j+=1
            if ''.join(stack) == s:
                return True
                break
            
            
        print(stack)

        
        return False
        