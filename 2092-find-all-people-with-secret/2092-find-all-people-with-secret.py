class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        knew = set([0, firstPerson])
        i=0
        m=len(meetings)

        while i<m:
            t = meetings[i][2]
            knewChain = defaultdict(list)
            people = set()

            while i<m and meetings[i][2]==t:
                p1,p2,_=meetings[i]
                knewChain[p1].append(p2)
                knewChain[p2].append(p1)
                people.add(p1)
                people.add(p2)
                i+=1
            q = deque([p for p in people if p in knew])
            visited=set()
            while q:
                x=q.popleft()
                for nbr in knewChain[x]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
            knew|=visited
        return list(knew)


        #approach is good but dfs fails here fo edge cases
        # meetings.sort(key=lambda x:x[2])
        # res = [0, firstPerson]
        # knew = set()
        # knew.add(0)
        # knew.add(firstPerson)

        # currtime = 0

        # knewChain = defaultdict(list)
        # for p1,p2,time in meetings:
        #     knewChain[p1].append((p2,time))
        
        # def dfs(firstPerson):
        #     nonlocal currtime
        #     for p2,t in (knewChain[firstPerson]):
        #         if firstPerson not in  knewChain:
        #             return
        #         if t<currtime:
        #             return 
        #         if t>=currtime and p2 not in knew:
        #             res.append(p2)
        #             knew.add(p2)
        #             currtime = t
        #             dfs(p2)
        
        #     return res

        return dfs(firstPerson)


        
