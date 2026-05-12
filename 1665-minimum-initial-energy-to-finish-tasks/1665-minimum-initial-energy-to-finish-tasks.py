class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # tasks.sort(reverse=True)
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True) #key part 
        # print(tasks)
        res = 0
        energy = 0
        initenergy = 0
        for actual, minimum in tasks:
            if energy < minimum:
                initenergy+=(minimum-energy)
                energy = minimum

            energy-=actual

        return initenergy