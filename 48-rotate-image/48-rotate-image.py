class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,len(matrix[0])):
                #print(i,j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    
        for i in range(n):
            for j in range(len(matrix)//2):
                print(i,j)
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix) - 1 - j]
                matrix[i][len(matrix) - 1 - j] = temp