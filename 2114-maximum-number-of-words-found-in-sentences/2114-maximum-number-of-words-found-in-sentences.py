class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0
        for i in sentences:
            sum=len(i.split(" "))
            if maximum<sum:
                maximum=sum
        return maximum