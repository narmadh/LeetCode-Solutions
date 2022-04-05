class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        num=nums1+nums2
        return num