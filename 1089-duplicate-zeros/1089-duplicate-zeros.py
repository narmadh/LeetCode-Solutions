class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        i=0
        count=0
        while(i<n):
            if arr[i]==0:
                arr.insert(i+1,0)
                count+=1
                i+=2
            else:
                i+=1
        #print(count)
        for j in range(count):
            arr.pop()