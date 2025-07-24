class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # for a,b in prerequisites:
        #     if [b,a] in prerequisites:
        #         return False
                
        for course, req in prerequisites:
            graph[course].append(req)

        visited=set() #all the course along the DFS path
        
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True #no requirements
            visited.add(course)
            for req in graph[course]:
                if not dfs(req): return False
            visited.remove(course)
            graph[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True    
        