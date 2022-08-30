class Solution:
    def Sqrt(self,x):
        if x < 2:
            return x
        i = 1
        j= (x//2) + 1
        res = 0
        while i <= j:
            mid = (i + j)//2
            if mid * mid <= x:
                res = mid
                i = mid + 1
            else:
                j = mid - 1
        return res
    def mySqrt(self, x: int) -> int:
        return self.Sqrt(x)