class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # possibleKCombinations = list(itertools.product(['0', '1'], repeat=k))
        # print(possibleKCombinations)
        seencombs = set()
        possiblecombs = 2**k
        
        for i in range(len(s)-k+1):
            sub = s[i:i+k]
            if sub not in seencombs:
                seencombs.add(sub)
            else:
                continue
        print(seencombs)
        return len(seencombs) ==  possiblecombs