class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText.rstrip()

        n = len(encodedText)
        cols = n // rows

        mat = []
        k=0
        for r in range(rows):
            row=[]
            for c in range(cols):
                row.append(encodedText[k])
                k+=1
            mat.append(row)
        
        res=[]
        for c in range(cols):
            r=0
            cc=c
            while r<rows and cc<cols:
                res.append(mat[r][cc])
                r+=1
                cc+=1
        
        return ''.join(res).rstrip()





        
        