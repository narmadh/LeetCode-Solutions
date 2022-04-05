class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maximum=nums[0]
        for i in range(len(nums)):
            sum+=nums[i]
            maximum=max(sum,maximum)
            if sum<0:
                sum=0
        return maximum