class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=(nums[i]-1)*(nums[j]-1)
                maximum=max(sum,maximum)
        return maximum