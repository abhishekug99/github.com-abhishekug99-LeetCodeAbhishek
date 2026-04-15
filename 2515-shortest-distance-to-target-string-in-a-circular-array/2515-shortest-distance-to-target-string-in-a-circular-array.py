class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        cnt1=0
        cnt2=0
        n = len(words)
        
        i=startIndex
        while True:
            if words[i] == target:
                break
            
            i = ((i + 1) % n)
            cnt1+=1
        
        i=startIndex
        while True:
            if words[i] == target:
                break
            
            i = ((i - 1 + n) % n)
            cnt2+=1
        
        return min(cnt1, cnt2)
