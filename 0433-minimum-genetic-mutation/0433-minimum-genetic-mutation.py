class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue =  deque()
        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue.append([startGene, 0])
        visited = set([startGene])
        while queue:
            gene,level = queue.popleft()
            if gene == endGene:
                return level
            for i in range(len(gene)):
                for g in "AGTC":
                    if g != gene[i]:
                        mutated = gene[:i]+g+gene[i+1:]
                        if mutated in bank and mutated not in visited:
                            visited.add(mutated)
                            queue.append([mutated,level+1])
        return -1
















        