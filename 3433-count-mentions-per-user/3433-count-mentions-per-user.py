class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        online = [True]*numberOfUsers
        backOnline = [-1]*numberOfUsers
        mensions = [0]*numberOfUsers #res
        allCnt = 0
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        for event in events:
            if "MESSAGE" == event[0]:
                if "ALL" == event[2]:
                    allCnt+=1
                elif "HERE" == event[2]:
                    time = int(event[1])
                    for i in range(numberOfUsers):
                        if online[i]<=time:
                            mensions[i]+=1
                else:
                    for sid in event[2].split():
                        mensions[int(sid[2:])]+=1
            else:
                online[int(event[2])] = int(event[1])+60
        
        for i in range(numberOfUsers):
            mensions[i]+=allCnt
        return mensions


        
        # Heap solution O(nlogn)
        # pq = [] #minheap
        # events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        # allCnt =0
        # for event in events:
        #     typ, ts, info = event
        #     ts = int(ts)
            
        #     while pq and pq[0][0]<=ts:
        #         retTime, u = heapq.heappop(pq)
        #         if backOnline[u] ==retTime:
        #             online[u] = True
        #     if typ == 'OFFLINE':
        #         u = int(info)
        #         online[u]=False
        #         retTime=ts+60
        #         backOnline[u] = retTime
        #         heapq.heappush(pq, (retTime, u))
        #     else:
        #         if info=="ALL":
        #             allCnt+=1
        #         elif info=="HERE":
        #             for u in range(numberOfUsers):
        #                 if online[u]:
        #                     mensions[u]+=1
        #         else:
        #             for t in info.split():
        #                 u=int(t[2:])
        #                 mensions[u]+=1
        # if allCnt:
        #     for u in range(numberOfUsers):
        #         mensions[u]+=allCnt
                
        # return mensions

        # good but not accepted, bugs
        # returnAt = defaultdict(list)
        # for event in events:
        #     typ, ts, info = event
        #     ts = int(ts)
            
        #     if ts in returnAt:
        #         for user in returnAt[ts]:    
        #             online[user] = True
        #         del returnAt[ts]
                
        #     if typ == 'OFFLINE':
        #         user = int(info) #as offline its will be int str
        #         online[user] = False
        #         returnAt[ts+60].append(user)

        #     else: #if online the third would some message
        #         mensionStr = info
        #         if mensionStr == 'ALL':
        #             for i in range(numberOfUsers):
        #                 mensions[i]+=1
        #         elif mensionStr == 'HERE':
        #             for i in range(numberOfUsers):
        #                 if online[i]:
        #                     mensions[i]+=1
        #         else:
        #             tocken = mensionStr.split()
        #             for t in tocken:
        #                 user = int(t[2:]) #id in form 'id0' 
        #                 mensions[user]+=1
        
        # return mensions