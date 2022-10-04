class Solution:
    def func(self,ind,s,path):
        if(ind==len(s)):
            self.res.append(path[:])
            return
        for i in range(ind,len(s)):
            if(self.isPalindrome(s,ind,i)):
                path.append(s[ind:i+1])
                self.func(i+1,s,path)
                path.pop()
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        path=[]
        self.func(0,s,path)
        return self.res
    def isPalindrome(self,s,i,j):
        while j>i:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True