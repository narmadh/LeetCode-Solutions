class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1=0
        p2=len(s)-1
        self.reverseString2(p1,p2,s)
    def reverseString2(self,p1,p2,s):
        if(p1>=p2):
            return s
        s[p1],s[p2]=s[p2],s[p1]
        self.reverseString2(p1+1,p2-1,s)
        