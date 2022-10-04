class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1=nums[:n]
        nums2=nums[n:]
        num=[]
    
        for i in range(len(nums1)):
            num.append(nums1[i])
            num.append(nums2[i])
        return num