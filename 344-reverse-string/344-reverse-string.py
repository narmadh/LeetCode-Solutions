class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1=0
        n=len(s)
        self.reverseString2(p1,n,s)
    def reverseString2(self,p1,n,s):
        if(p1>=n-p1-1):
            return s
        s[p1],s[n-p1-1]=s[n-p1-1],s[p1]
        self.reverseString2(p1+1,n,s)
        