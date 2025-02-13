class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumMap = {}  # Hashmap to store max num for each digit sum
        maxSum = -1  # Track the max sum of valid pairs

        for num in nums:
            digitSum = sum(map(int, str(num)))  # Compute sum of digits
            
            if digitSum in sumMap:
                maxSum = max(maxSum, num + sumMap[digitSum])  # Compare max sum
            
            sumMap[digitSum] = max(sumMap.get(digitSum, 0), num)  # Store max num for this digit sum

        return maxSum
        
        # brutforce 54/83
        # res =[]
        # for i in range(len(nums)):
        #     while j<i:
                
        #         print(list(map(int, str(nums[i]))))
        #         if  sum(list(map(int, str(nums[i])))) == sum(list(map(int, str(nums[j])))):
        #             res.append(nums[i] + nums[j])
        #         j+=1
        # if res:
        #     return max(res)
        # else:
        #     return -1
                