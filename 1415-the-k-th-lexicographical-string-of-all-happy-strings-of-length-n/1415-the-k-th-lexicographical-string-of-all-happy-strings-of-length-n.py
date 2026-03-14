class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n==1:
            res = 'abc'
            return res[k-1] if k<=3 else ''
        possible = itertools.product('abc', repeat=n)
        
        happies = []

        def ishappy(tup):
            for i in range(n-1):
                if tup[i]==tup[i+1]:
                    return False
            return True

        for tup in possible:
            if ishappy(tup):
                happies.append(tup)
        
        # print(len(happies))
        return ''.join(happies[k-1]) if len(happies)>=k else  '' 
              