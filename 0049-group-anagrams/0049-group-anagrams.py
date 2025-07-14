class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
    
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
            
        print(anagrams)
        
        return list(anagrams.values())
        
        
        # if len(strs) == 1:
        #     return [[strs[0]]]
        # if not strs:
        #     return [['']]
        # def isAnagram(w1,w2) -> bool:
        #     gw1={}
        #     gw2={}
        #     if len(w1)!=len(w1):
        #         return False
        #     return (list(w1)).sort() == (list(w2)).sort() 
            
        # res = []
        # stack = []
        # i=0
        # while i < (len(strs)):
        #     tmp = [strs[i]]
        #     j=i+1
        #     while j<len(strs):
        #         if isAnagram(strs[i],strs[j]) and strs[j] not in stack:
        #             tmp.append(strs[j])
        #             stack.append(strs[j])
        #         j+=1
        #     res.append(tmp)
        #     i+=1
        # return res
