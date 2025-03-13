class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #optimised version
        #using Counter
        if len(word1) != len(word2):
            return False
        w1Cnt = Counter(word1)
        w2Cnt = Counter(word2)
        
        if set(w1Cnt.keys()) == set(w2Cnt.keys()) and sorted(w1Cnt.values()) == sorted(w2Cnt.values()):
            return True
        
        return False

        
        #beats 5.32% only
        # graphW1 = {}
        # graphW2 = {}
        # if len(word1) != len(word2):
        #     return False
        
        # for i in range (len(word1)):
        #     if word1[i] not in graphW1:
        #         graphW1[word1[i]] = 1
        #     else:
        #         graphW1[word1[i]] += 1
        # for i in range (len(word2)):
        #     if word2[i] not in graphW2:
        #         graphW2[word2[i]] = 1
        #     else:
        #         graphW2[word2[i]] += 1
        
        # if sorted(graphW1.keys()) == sorted(graphW2.keys()) and sorted(graphW1.values()) == sorted(graphW2.values()):
        #     return True

        # else: return False