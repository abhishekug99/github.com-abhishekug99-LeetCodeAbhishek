class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(' ')
        res =[]
        # print(sList)
        # for w in sList:
        #     if w == '':
        #         sList.remove('')
        sList = list(filter(None, sList))
        print(sList)
        while not sList == []:       
            res.append(sList.pop())
            # print(sList)

        
        return ' '.join(map(str, res))

        