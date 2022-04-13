class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(ind,array,target,ans):
            
            if ind == len(array):
                if target == 0:
                    nonlocal res
                    res.append(copy.deepcopy(ans))
                    
                return 
            
            if array[ind] <= target:
                ans.append(array[ind])
                func(ind,array,target-array[ind],ans)
                ans.remove(array[ind])
                
            func(ind+1,array,target,ans)
            
            
        res = []
        ans = []
        func(0,candidates,target,ans)
        return res