class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]==0:
                a=arr.count(0)
                print(a)
                if a==2:
                    return True
                else:
                    continue
            if arr[i]*2 in arr:
                return True
        return False
        