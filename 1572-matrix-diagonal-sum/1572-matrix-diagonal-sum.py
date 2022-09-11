class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        priDiagonal=0
        secDiagonal=0
        n=len(mat[0])
        dSum=0
        for i in range(len(mat)):
            dSum+=mat[i][i]
            if n-1-i!=i:
                dSum+=mat[i][n-1-i]
            
        #dSum=priDiagonal+secDiagonal
        return dSum
            