class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        graph = defaultdict(int)
        l,total, res=0,0,0

        for i in range(len(fruits)):
            graph[fruits[i]]+=1
            total += 1
            while len(graph)>2:
                f = fruits[l]
                graph[f]-=1
                total-=1
                l+=1

                if not graph[f]:
                    graph.pop(f)


            res = max(res,total)


        return res