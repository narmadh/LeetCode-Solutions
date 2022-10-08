class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashTable={}
        for i in range(len(names)):
            hashTable[heights[i]]=names[i]
        heights.sort(reverse=True)
        res = []
        for height in heights:
            res.append(hashTable[height])
        return res