class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat[0])
        k %= m

        newMat = []

        for i, row in enumerate(mat):
            if i % 2 == 0:  
                newMat.append(row[k:] + row[:k])
            else:           
                newMat.append(row[-k:] + row[:-k])

        return newMat == mat

