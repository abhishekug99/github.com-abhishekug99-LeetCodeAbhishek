class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        minPenalty = penalty
        bestHr = 0

        for i,c in enumerate(customers):
            if c == 'Y':
                penalty-=1
            else:
                penalty+=1

            if  minPenalty>penalty:
                minPenalty = penalty
                bestHr = i+1
        return bestHr
        
        
        
        
        # if 'Y' not in customers:
        #     return 0
        # if 'N' not in customers:
        #     return len(customers)

        # hrToPenalty = {}
        # n = len(customers)
        # closed = [[False]*n for _ in range(n)]

        # for j in range(len(customers)):
        #     closed[j][j] = True
        #     for i in range(len(customers)):
        #         if closed[j][i] == True:
        #             hrToPenalty[j] = hrToPenalty.get(j, 0) + 1
        #         elif closed[j][i] == True and customers[i]=='Y':
        #             hrToPenalty[j] = hrToPenalty.get(j, 0) + 1
        #         elif customers[i] == 'N' and closed[j][i] == False:
        #             hrToPenalty[j] = hrToPenalty.get(j, 0) + 1
        # minVal  = min(list(hrToPenalty.values()))
        # for k,v in hrToPenalty.items():
        #     if hrToPenalty[k]==minVal:
        #         return k
        #         break
        

