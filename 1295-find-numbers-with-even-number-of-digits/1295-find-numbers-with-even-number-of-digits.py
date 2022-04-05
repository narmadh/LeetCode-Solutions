class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            count=0
            while(nums[i]>0):
                
                count+=1
                nums[i]=nums[i]//10
            if count%2==0:
                ans+=1
        return ans