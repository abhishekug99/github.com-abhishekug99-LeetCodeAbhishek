class Solution:
    def hIndex(self, citations: List[int]) -> int:      
        citations.sort(reverse = True)
        for i in range(len(citations)):
            
            if i+1 > citations[i]:
                return i

        return len(citations)

        # for i in range(len(citations)-1,-1,-1):
        #     curSum +=citations[i]
        #     if curSum <= len(citations[:i]):
        #         res.append(citations[i])
        # print(res)
        # return max(res) if res else 0