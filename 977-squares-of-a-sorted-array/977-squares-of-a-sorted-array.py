class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            nums2.append(nums[i]**2)
        nums2.sort()
        return nums2