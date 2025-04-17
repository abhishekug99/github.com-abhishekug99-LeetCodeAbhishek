class Solution:
    def isValid(self, s: str) -> bool:
        parMapping = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for par in s:
            if par in parMapping:
                stack.append(par)
            elif not stack or parMapping[stack.pop()]!=par:
                return False
        if stack:
            return False
        return True
        # return not stack #works as well

