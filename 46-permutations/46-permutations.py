class Solution:
    def helper(self,ds,map,arr,ans):
        if (len(ds)==len(arr)):
            ans.append(ds.copy())
            return ans
        for i in range(0,len(arr)):
            if(map[i]==False):
                map[i]=True
                ds.append(arr[i])
                self.helper(ds,map,arr,ans)
                ds.pop(-1)
                map[i]=False
    def permute(self, nums: List[int]) -> List[List[int]]:
        map={}
        ans=[]
        for i in range(len(nums)):
            map[i]=False
        self.helper([],map,nums,ans)
        return ans