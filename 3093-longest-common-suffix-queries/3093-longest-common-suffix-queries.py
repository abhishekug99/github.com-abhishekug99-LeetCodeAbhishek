import heapq
class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        #with trie
        root = TrieNode()
        def better(i, j):
            """
            return better index between i and j
            """
            if j == -1:
                return i

            if len(wordsContainer[i]) < len(wordsContainer[j]):
                return i

            if len(wordsContainer[i]) > len(wordsContainer[j]):
                return j

            return min(i, j)

        # build trie
        for i, word in enumerate(wordsContainer):

            node = root

            # update root
            node.idx = better(i, node.idx)

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                node.idx = better(i, node.idx)

        res = []

        # process queries
        for q in wordsQuery:

            node = root

            for ch in reversed(q):

                if ch not in node.children:
                    break

                node = node.children[ch]

            res.append(node.idx)

        return res
        
        
        #TLE 807 / 817 testcases passed
        # n = len(wordsContainer)
        # default_idx = min(range(n), key=lambda i: (len(wordsContainer[i]), i))

        # res = []

        # for q in wordsQuery:

        #     best_suffix = -1
        #     best_len = float('inf')
        #     best_idx = default_idx

        #     for i, w in enumerate(wordsContainer):

        #         k = 0

        #         while (k < len(q) and k < len(w) and q[-1-k] == w[-1-k]):
        #             k += 1
        #         if k > best_suffix:
        #             best_suffix = k
        #             best_len = len(w)
        #             best_idx = i

        #         elif k == best_suffix:

        #             if len(w) < best_len:
        #                 best_len = len(w)
        #                 best_idx = i

        #             elif len(w) == best_len and i < best_idx:
        #                 best_idx = i

        #     res.append(best_idx)

        # return res

        #bruteforce, not worked
        # n = len(wordsContainer)
        # m = len(wordsQuery)
        # res = [0]*m
        # mappres = defaultdict(list)
        # for i in range(m):
        #     for j in range(n):
        #         pre = wordsQuery[i]
        #         word = wordsContainer[j]
        #         if word.endswith(pre):
        #             heapq.heappush(mappres[pre], (len(word), j, word))
        # # print(mappres)

        # curr = 0
        # i=0 
        # for i, q in enumerate(wordsQuery):
        #     heap = mappres[q]
        #     # print(heap)
        #     if heap:
        #         le, idx, st = heapq.heappop(heap)
        #         res[i] = idx

        #     else:
        #         best = min(
        #             range(n),
        #             key=lambda x: (len(wordsContainer[x]), x))
        #         res[i] = best
        
        # return res
