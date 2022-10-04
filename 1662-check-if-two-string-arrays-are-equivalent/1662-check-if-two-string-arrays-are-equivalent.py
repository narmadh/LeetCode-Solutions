class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        strWord1=""
        strWord2=""
        for i in range(len(word1)):
            strWord1=strWord1+word1[i]
        for i in range(len(word2)):
            strWord2=strWord2+word2[i]

        if strWord1==strWord2:
            return True
        else:
            return False