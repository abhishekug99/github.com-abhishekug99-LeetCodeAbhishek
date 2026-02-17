class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)

        for word in words:
            waiting[word[0]].append(word)
        
        res = 0
        # print(waiting)
        for c in s:
            word_waiting = waiting[c]
            waiting[c] = deque()
            # print(waiting)
            while word_waiting:
                w = word_waiting.popleft()
                if len(w)==1:
                    res+=1
                else:
                    waiting[w[1]].append(w[1:])
        return res


            
            