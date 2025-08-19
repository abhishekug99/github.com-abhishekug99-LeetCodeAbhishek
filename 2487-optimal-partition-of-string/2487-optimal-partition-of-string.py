class Solution:
    def partitionString(self, s: str) -> int:
        #optimised to O(n) and extra space
        visited = set()
        cnt =1
        for ch in s:
            if ch in visited:
                cnt+=1
                visited.clear()
            visited.add(ch)
        return cnt
                
        
        #Accepted ans works in O(n^2) and extra space
        # i=0 
        # subSList = []
        # while i< len(s):
        #     subS = s[i]
        #     j=i+1
        #     while j<len(s):
        #         if s[j] not in  subS:
        #             subS += s[j]
        #         else:
        #             break
        #         j+=1
        #     subSList.append(subS)
        #     i=j   
        # print(subSList)
        # return len(subSList)
