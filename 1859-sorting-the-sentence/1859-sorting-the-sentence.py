class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        word1=[0]*len(words)
        for i in words:
            ind=int(i[-1])-1
            indValue=i[:-1]
            word1[ind]=indValue
        sentence=" ".join(word1)
        return sentence