class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cntRN = Counter(ransomNote)
        cntMZ = Counter(magazine)
        if len(cntRN) ==1 and len(cntMZ) == 1 and ransomNote != magazine:
            return False
        

        for k,v in cntRN.items():
            if v >  cntMZ[k]:
                return False
        
        return True