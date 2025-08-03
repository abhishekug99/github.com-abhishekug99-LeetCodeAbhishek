class TrieNode:
    def __init__(self):
        self.child = {}
        self.endOfWord = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.endOfWord = True


    def search(self, word: str) -> bool:   
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            ch = word[i]
            if ch =='.':
                for child in node.child.values():
                    if dfs(child, i+1):
                        return True
                return False
            else:
                if ch not in node.child:
                    return False
                return dfs(node.child[ch], i+1)
    
        return dfs(self.root, 0)


    # works O(n^2), TLE
    # def __init__(self):
    #     self.res = []

    # def addWord(self, word: str) -> None:
    #     self.res.append(word)

    
    # def search(self, word: str) -> bool:
    #     for w in self.res:
    #         if len(w)!=len(word):
    #             continue
    #         match = True
    #         for wc, qc in zip(w,word):
    #             if qc != '.' and wc!=qc:
    #                 match  = False
    #                 break
    #         if match:
    #             return True
    #     return False
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)