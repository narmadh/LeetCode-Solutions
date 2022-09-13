class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        rangeSum=(n*(n+1))//2
        realSum=0
        for i in nums:
            realSum+=i
        return rangeSum-realSum