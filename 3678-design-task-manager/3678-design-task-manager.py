# Max time is (log(n)) for add and edit using heap
import heapq
from typing import List

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap = []  # (-priority, -taskId, userId, taskId)
        self.taskMap = {}  # taskId -> (priority, userId)

        for uId, tId, prio in tasks:
            self._add_task(uId, tId, prio)

    def _add_task(self, userId: int, taskId: int, priority: int):
        self.taskMap[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self._add_task(userId, taskId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.taskMap:
            return
        userId = self.taskMap[taskId][1]
        self._add_task(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]

    def execTop(self) -> int:
        while self.heap:
            prio, negTid, userId, taskId = heapq.heappop(self.heap)
            # validate against current record
            if taskId in self.taskMap:
                priority, uid = self.taskMap[taskId]
                if priority == -prio and uid == userId:
                    # valid → execute
                    del self.taskMap[taskId]
                    return userId
        return -1




#correct but O(n) TLE 
# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         self.tasks = tasks
#         self.taskMap = {}
#         for i, (uId, tId, prio) in enumerate(tasks):
#             self.taskMap[tId] = [i, uId, prio]

#     def add(self, userId: int, taskId: int, priority: int) -> None:
#         n = len(self.tasks)
#         newtask = [userId, taskId,priority]
#         self.tasks.append(newtask)
#         self.taskMap[taskId] = [n, userId,priority]


#     def edit(self, taskId: int, newPriority: int) -> None:
#         if taskId not in self.taskMap:
#             return
#         idx, uId,_ = self.taskMap[taskId]
#         self.taskMap[taskId][2] = newPriority
#         self.tasks[idx] = [uId, taskId, newPriority] 
        

#     def rmv(self, taskId: int) -> None:
#         if taskId not in self.taskMap:
#             return
#         idx = self.taskMap[taskId][0]
#         self.tasks.pop(idx)
#         del  self.taskMap[taskId]
#         #rebuild the map
#         self.taskMap.clear()
#         for i, (uId, tId, prio) in enumerate(self.tasks):
#             self.taskMap[tId] = [i, uId, prio]
        

#     def execTop(self) -> int:
#         if not self.taskMap:
#             return -1

#         maxPriority = -10**18
#         chosenTaskId = -10**18
#         chosenUid = -1

#         # find the candidate with highest priority, and if tie use larger taskId
#         for tId, (idx, uId, prio) in self.taskMap.items():
#             if prio > maxPriority or (prio == maxPriority and tId > chosenTaskId):
#                 maxPriority = prio
#                 chosenTaskId = tId
#                 chosenUid = uId

#         # remove the chosen task by its index, and rebuild mapping
#         chosen_idx = self.taskMap[chosenTaskId][0]
#         self.tasks.pop(chosen_idx)
#         del self.taskMap[chosenTaskId]

#         self.taskMap.clear()
#         for i, (uId, tId, prio) in enumerate(self.tasks):
#             self.taskMap[tId] = [i, uId, prio]

#         return chosenUid
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()