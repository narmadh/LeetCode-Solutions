class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        c=0
        
        for i in range(len(s)):
            if s[i]=="R":
                r+=1
            if s[i]=="L":
                l+=1
                
            if r==l:
                c+=1
                
        return c
