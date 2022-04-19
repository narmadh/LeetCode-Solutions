class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = [['.'] * n for _ in range(n)] 
        self.backtracking(n, 0, cur, res)
        return res
    
    def backtracking(self, n, row, cur, res):
        if row == n:
            res.append([''.join(cur[i]) for i in range(n)])
            return
        
        for j in range(n):
            if not self.is_valid(row, j, cur):
                continue
            cur[row][j] = 'Q'
            self.backtracking(n, row + 1, cur, res)
            cur[row][j] = '.'
    
    def is_valid(self, m, n, cur):
        for i in range(m):
            if cur[i][n] == 'Q':
                return False
            if n + m - i < len(cur) and cur[i][n + m - i] == 'Q':
                return False
            if n - m + i >= 0 and cur[i][n - m + i] == 'Q':
                return False
        
        return True