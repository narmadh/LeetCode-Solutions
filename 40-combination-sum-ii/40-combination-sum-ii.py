class Solution:
    
                
                
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def findCombination(ind,arr,target,ans,ds):
            if(target==0):
                ans.append(ds.copy())
                return
            for i in range(ind,len(arr)):
                if(i>ind) and (arr[i]==arr[i-1]):
                    continue
                if arr[i]>target:
                    break
                ds.append(arr[i])
                findCombination(i+1,arr,target-arr[i],ans,ds)
                ds.pop(-1)
        
        findCombination(0,candidates,target,ans,[])
        return ans