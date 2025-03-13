class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        graphW1 = {}
        graphW2 = {}
        if len(word1) != len(word2):
            return False
        
        for i in range (len(word1)):
            if word1[i] not in graphW1:
                graphW1[word1[i]] = 1
            else:
                graphW1[word1[i]] += 1
        for i in range (len(word2)):
            if word2[i] not in graphW2:
                graphW2[word2[i]] = 1
            else:
                graphW2[word2[i]] += 1
        
        # print(graphW1)
        # print(graphW2)
        # print(list(graphW1.values()))
        # print(list(graphW2.values()))
        # print(sorted(list(graphW1.keys())))
        # print(sorted(list(graphW2.keys())))
        
        if sorted(graphW1.keys()) == sorted(graphW2.keys()) and sorted(graphW1.values()) == sorted(graphW2.values()):
            return True

        else: return False