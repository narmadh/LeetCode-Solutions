class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        cols=len(matrix[0])
        res=[[None]*rows for k in range(cols)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i]=matrix[i][j]
        return res