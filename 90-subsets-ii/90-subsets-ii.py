class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def findCombination(ind,arr,ans,ds):
            ans.append(ds.copy())    
            for i in range(ind,len(arr)):
                if(i!=ind and arr[i]==arr[i-1]):
                    continue
                ds.append(arr[i])
                findCombination(i+1,arr,ans,ds)
                ds.pop(-1)
        
        findCombination(0,nums,ans,[])
        return ans