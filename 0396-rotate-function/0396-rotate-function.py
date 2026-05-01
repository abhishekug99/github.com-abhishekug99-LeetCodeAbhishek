class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        # F(0)
        f = sum(i * nums[i] for i in range(n))
        ans = f

        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)

        return ans
            
        #works but TLE
        # n = len(nums)
        # res = [0] * n

        # def f(k):
        #     s = 0
        #     for i in range(n):
        #         s+=i*nums[(i+k)%n]
        #     return s

        # for k in range(n):
        #     res[k] = f(k)
        
        # return max(res)
      

