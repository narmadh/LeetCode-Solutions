class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(mat,target):
            low = 0
            high = len(mat)-1
            while low <= high:
                mid=(low + high)//2
                if mat[mid] == target:
                    return True
                elif target < mat[mid]:
                    high = mid-1
                elif target > mat[mid]:
                    low = mid+1
            return False
        for i in range(len(matrix)):
            if search(matrix[i],target)==True:
                return True    
        return False