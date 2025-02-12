class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            index = s.find(part)  
            print(index)
            s = s[:index] + s[index + len(part):]  
        return s
        
        # works for 78/80 test case
        # new = s.replace(part,'')
        # while new != s:
        #     s = new
        #     new = s.replace(part,'')
        # return new

            