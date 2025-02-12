class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_map = {}  # Hashmap to store max num for each digit sum
        max_sum = -1  # Track the max sum of valid pairs

        for num in nums:
            digit_sum = sum(map(int, str(num)))  # Compute sum of digits
            
            if digit_sum in sum_map:
                max_sum = max(max_sum, num + sum_map[digit_sum])  # Compare max sum
            
            sum_map[digit_sum] = max(sum_map.get(digit_sum, 0), num)  # Store max num for this digit sum

        return max_sum
        
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
                