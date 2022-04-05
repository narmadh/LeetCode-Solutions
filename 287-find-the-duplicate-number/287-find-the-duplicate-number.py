class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freArr=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            if freArr[nums[i]]==0:
                freArr[nums[i]]+=1
            else:
                return nums[i]