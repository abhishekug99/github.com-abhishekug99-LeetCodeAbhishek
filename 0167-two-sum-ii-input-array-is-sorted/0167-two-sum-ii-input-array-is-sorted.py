class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        i = 0
        j = len(numbers)-1

        while i<j:
            currTarget = numbers[i] + numbers[j]
            if currTarget == target:
                res.append(i+1)
                res.append(j+1)
                break
            elif currTarget < target:
                i+=1
            else:
                j-=1
        
        return res


        #correct-bruteforce tle
        # for i in range(len(numbers)):
        #     j=i+1
        #     while j<len(numbers):
        #         if numbers[i] + numbers[j] == target:
        #             res.append(i+1)
        #             res.append(j+1)
        #             break
        #         j+=1
            
        # return res


        