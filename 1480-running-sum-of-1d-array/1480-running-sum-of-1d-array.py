class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        val=0
        for i in range(len(nums)):
            val+=nums[i]
            ans.append(val)
        return ans