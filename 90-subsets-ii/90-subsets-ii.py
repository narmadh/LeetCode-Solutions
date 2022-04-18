class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def findCombination(ind,arr,ans,ds):
            if(ind>=len(arr)):
                ans.append(ds.copy())
                return
            ds.append(arr[ind])
            findCombination(ind+1,arr,ans,ds)
            ds.pop(-1)
            findCombination(ind+1,arr,ans,ds)
            
        
        findCombination(0,nums,ans,[])
        res=[]
        for i in ans:
            if i not in res:
                res.append(i)
        return res