class Solution:
    def trap(self, height: List[int]) -> int:
        # if len(height)==0:
        #     return 0
        
        # maxL = [0] *len(height)
        # maxR = [0] *len(height)

        # maxL[0] = height[0]
        # for i in range(1, len(height)):
        #     maxL[i] = max(maxL[i-1], height[i])
        
        # maxR[-1] = height[-1]    
        # for i in range(len(height)-2, -1,-1):
        #     maxR[i] = max(maxR[i+1], height[i])

        # res=0
        # for i in range(len(maxL)):
        #     res += (min(maxL[i],maxR[i])-height[i])

        # return res

        #withought extra space: bianary dearch approch
        if not height: return 0
        l,r  = 0, len(height)-1
        res = 0
        lMax = height[l]
        rMax = height[r]
        while l<r:
            if lMax<rMax:
                l+=1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r-=1
                rMax = max(rMax, height[r])
                res+= rMax - height[r]
        return res

