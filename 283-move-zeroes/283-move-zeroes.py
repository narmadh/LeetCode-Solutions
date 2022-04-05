class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        n=0
        for i in range(len(nums)):
            if nums[i]==0:
                n+=1
            elif nums[i]!=0  and n!=0:
                nums[i-n]=nums[i]
                nums[i]=0