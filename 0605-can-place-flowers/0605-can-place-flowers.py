class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        lenght = len(flowerbed)

        for i in range(lenght):
            if flowerbed[i]==0:
                lZero = (i==0 or flowerbed[i-1]==0)
                rZero = (i==len(flowerbed)-1 or flowerbed[i+1]==0)

                if lZero and rZero:
                    flowerbed[i]=1 
                    cnt+=1
                    if cnt>=n:
                        return True
        return cnt>=n
        
        # goes for 110 test cases
        # cnt = 0
        # for i in range(1,len(flowerbed)-1):
        #     if flowerbed[i-1] !=1 and flowerbed[i+1] != 1 and flowerbed[i]!=1:
        #         flowerbed[i] = 1
        #         cnt+=1
        # print(n)
        # if cnt >= n:
        #     return  True
        # return False