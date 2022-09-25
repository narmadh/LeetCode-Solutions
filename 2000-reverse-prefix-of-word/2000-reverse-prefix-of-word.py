class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j=0
        for i in word:
            j+=1
            if i==ch:
                break
            elif j==len(word):
                return word
        j=j-1
        i=0
        w=list(word)
        print(w,j,i)
        while(i<j):
            w[i],w[j]=w[j],w[i]
            i+=1
            j-=1
        return "".join(w)