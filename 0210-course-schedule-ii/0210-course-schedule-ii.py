class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for i in range(numCourses):
            graph[i] = []

        for course, req in prerequisites:
            graph[course].append(req)

        visited=set() #all the course along the DFS path
        finished = set()
        res = []
        def dfs(course):
            if course in visited:
                return False
            if course in finished:
                return True
            # if graph[course] == []:
            #     return True #no requirements
             

            visited.add(course)
            for req in graph[course]:
                if not dfs(req): return False
            visited.remove(course)
            graph[course] = []
            finished.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res