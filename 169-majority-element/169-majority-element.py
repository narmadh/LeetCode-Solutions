class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=0
        for i in range(0,len(nums)):
            if(count==0):
                candidate=nums[i]
            if nums[i]==candidate:
                count+=1
            else:
                count-=1
        return candidate