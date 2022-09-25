class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        for i in range(len(l)):
            left=0
            right=len(l[i])-1
            tmp=list(l[i])
            while(left<=right):
                tmp[left],tmp[right]=tmp[right],tmp[left]
                right-=1
                left+=1
            l[i]="".join(tmp)
        return " ".join(l)