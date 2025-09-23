class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        # print(v1)
        # print(v2)
        while len(v1)<len(v2):
            v1.append(0)
        while len(v2)<len(v1):
            v2.append(0)

        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        return 0



        # if int(v1[0])>int(v2[0]):
        #     return -1
        # if int(v1[0])<int(v2[0]):
        #     return 0
        
        # i=1
        # while i < max(len(v1), len(v2)):
        #     if i<len(v1) and i<len(v2):
        #         if (int(v1[i]) <= int(v2[i])):
        #             continue
        #         elif  (int(v1[i]) > int(v2[i])):
        #             reuturn -1
        #     if len(v1)>=i and len(v2)<=i:
        #         if int(v1[-1]) <= int(v2[i-1]):
        #             return 0
        #         else:
        #             return -1
        #     i+=1
        # return 0
