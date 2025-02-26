class Solution:
    #dqueue approach greedy
    def predictPartyVictory(self, senate: str) -> str:
        dire,radiant = deque(), deque()
        for i, char in enumerate(senate):
            if char == 'D':
                dire.append(i)
            if char == 'R':
                radiant.append(i)

        while dire and radiant:
            dOne = dire.popleft()
            rOne = radiant.popleft()

            if dOne > rOne:
                radiant.append( rOne+len(senate))
            if dOne < rOne:
                dire.append( dOne+len(senate))
        if dire:
            return 'Dire'
        else:
            return 'Radiant'




    #regular aprroach O(n) 48/83
    # def predictPartyVictory(self, senate: str) -> str:
    #     if len(senate)==1 and senate[0] =='D':
    #         return 'Dire'
    #     if len(senate)==1 and senate[0] =='R':
    #         return 'Radiant'

    #     rightsQueue = [(char, 1) for char in senate]
    #     # print(rightsQueue)

    #     for i in range(len(rightsQueue)):
    #         if (rightsQueue[i][0]=='D' or rightsQueue[i][0]== 'R') and rightsQueue[i][1] == 1 and  i != len(rightsQueue)-1:
    #             rightsQueue[i+1] = (rightsQueue[i][0], 0)

    #         if i == len(rightsQueue)-1 and rightsQueue[i][1] == 1 and rightsQueue[0][1]==1:
    #             rightsQueue[0] = (rightsQueue[0][0], 0)
    #     print(rightsQueue)

    #     for i in range(len(rightsQueue)):
    #         if rightsQueue[i][0] == 'D' and rightsQueue[i][1] == 1:
    #             return 'Dire'
    #         elif rightsQueue[i][0] == 'R' and rightsQueue[i][1] == 1:
    #             return 'Radiant' 

