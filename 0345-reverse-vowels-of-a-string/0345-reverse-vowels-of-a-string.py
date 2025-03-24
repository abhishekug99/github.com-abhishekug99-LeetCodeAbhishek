class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u', 'A','E', 'I', 'O', 'U']
        stack = []
        sList = list(s)
        for i in range(len(sList)):
            if sList[i] in vowels:
                stack.append(sList[i])
        
        for i in range(len(sList)):
            if sList[i] in vowels:
                sList[i] = stack.pop()
        
        return ''.join(sList)
        