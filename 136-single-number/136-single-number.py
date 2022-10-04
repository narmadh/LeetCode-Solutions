class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        diction={}
        for i in range(len(nums)):
            if nums[i] in diction:
                diction[nums[i]]+=1
            else:
                diction[nums[i]]=1
        print(diction)
        for i,j in diction.items():
            if j==1:
                return i