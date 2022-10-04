class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        nums1=[]
        for i in range(len(nums)):
            nums1.insert(index[i],nums[i])
        return nums1