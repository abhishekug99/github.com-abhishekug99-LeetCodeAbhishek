import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2

        if len(B)<len(A):
            A,B = B,A
        
        l,r = 0, len(A) -1

        while True:
            i = (l+r)//2 #A
            j = half - i - 2 #B
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1)<len(A)  else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B)  else float('inf')

            if Aleft<=Bright and Bleft<=Aright:
                #odd
                if total%2:
                    return min(Aright, Bright)
                #even  
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
        



        
        
        # for num in nums2:
        #     idx = bisect.bisect_left(nums1, num)
        #     nums1.insert(idx, num)
        # print(nums1[-1]+nums1[0])
        
        # if len(nums1) %2 != 0:
        #     return nums1[len(nums1)//2]
        
        # res  = (nums1[len(nums1)//2] +  nums1[(len(nums1)//2)-1])/2
        # return res

        