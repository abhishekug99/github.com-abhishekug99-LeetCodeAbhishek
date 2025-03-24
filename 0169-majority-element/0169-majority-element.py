class Solution(object):
    def majorityElement(self, nums):
        # l = 0
        # r = 1
        # count  = 0
        # maxAppear = {}
        # maxappearIndex = 0
        # nums.sort()
        # if len(nums)<=1:
        #     return nums[0]

        # for i in range(len(nums)-1):
        #     if nums[l] == nums[r]:
        #         maxAppear[nums[i]] = count
        #         count  = count + 1
        #     else:
        #         l=r
        #     r = r+1
        # return  max(maxAppear, key= lambda x: maxAppear[x])

        #2
        if len(nums)<=1:
            return nums[0]
    
        cntAppearance = Counter(nums)
        return max(cntAppearance, key= lambda x: cntAppearance[x])

        #3
        # count = {}
        # result = 0
        # maxAppear =0
        # for number in nums:
        #     count[number] = 1+count.get(number,0)
        #     result = number if count[number] > maxAppear else result
        #     maxAppear = max(count[number], maxAppear)
        # return result


            


        """
        :type nums: List[int]
        :rtype: int
        """
        