class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort(reverse=True)
        for i in range(len(happiness)):
            if k and (happiness[i]-i)>=0:
                # print(happiness[i])
                res+=(happiness[i]-i)
                print(res)
                k-=1
            elif k==0:
                return res
        return res
