class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bits=[]
        for i in range(len(nums)):
            if nums[i][i]=='0':
                bits.append('1')
            else:
                bits.append('0')
            # print(bits)
        return ''.join(bits)
        
        # combinations = itertools.product('01', repeat=len(nums[0]))
        # # print(list(combinations))
        # for tup in combinations:
        #     if ''.join(tup) not in nums:
        #         return ''.join(tup)
    