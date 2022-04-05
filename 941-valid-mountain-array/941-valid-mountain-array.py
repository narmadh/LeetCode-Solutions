class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        i=1
        while(i<n and arr[i]>arr[i-1]):
            i+=1
        if i==1 or i==n:
            return False
        
        while(i<n and arr[i]<arr[i-1]):
            i+=1
        return i==len(arr)