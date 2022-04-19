class Solution:
    def recurPermute(self,ind,nums,ans):
        if(ind==len(nums)):
            ds=[]
            for i in range(len(nums)):
                ds.append(nums[i])
            ans.append(ds.copy())
            return
        for i in range(ind,len(nums)):
            self.swap(ind,i,nums)
            self.recurPermute(ind+1,nums,ans)
            self.swap(ind,i,nums)
    
    def swap(self,ind,i,nums):
        nums[i],nums[ind]=nums[ind],nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.recurPermute(0,nums,ans)
        return ans