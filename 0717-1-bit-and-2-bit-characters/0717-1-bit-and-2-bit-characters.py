class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        while i<len(bits)-1:
            i+=1+bits[i]
        return i == len(bits)-1
    

        # works great 0ms
        # i=0
        # while i<len(bits)-1:
        #     if bits[i] == 1:
        #         i+=2
        #     else:
        #         i+=1
        # return i == len(bits)-1
    