class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = len(apple)
        m = len(capacity)
        totalApples = sum(apple)
        res = 1
        if totalApples in capacity:
            return 1
        if totalApples >= sum(capacity):
            return len(capacity)
        
        capacity.sort(reverse=True)
        for i in range(m):
            if capacity[i]<totalApples:
                res+=1
                totalApples-=capacity[i]
            elif capacity[i]>=totalApples:
                return res
        return res
            
        