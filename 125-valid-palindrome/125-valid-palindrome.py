class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=set("abcdefghijklmnopqrstuvwxyz0123456789")
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] not in a:
                i+=1
                continue
            if s[j] not in a:
                j-=1
                continue
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True