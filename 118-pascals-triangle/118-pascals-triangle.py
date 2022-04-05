class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalTri=[]
        preRow=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if (j==0 or j==i):
                    row.append(1)
                else:
                    row.append(preRow[j-1]+preRow[j])
            preRow=row
            pascalTri.append(row)
        return pascalTri
                    