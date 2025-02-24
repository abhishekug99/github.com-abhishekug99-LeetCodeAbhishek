class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = 0
        sums = []
        sums.append(0)
        for i in range(len(gain)):
            if i == 0:
                gain[i] = gain[0]
                sums.append(gain[i])
            if i > 0:
                 gain[i] += gain[i-1]
                 sums.append(gain[i])

        return max(sums) 