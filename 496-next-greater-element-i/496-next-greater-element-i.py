import sys
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        i=0       
        while i<len(nums1):
            j=0
            value=sys.maxsize
            flag=False
            while (j<len(nums2)):
                if nums1[i]==nums2[j]:
                    value=nums2[j]
                if nums2[j]>value:
                    ans.append(nums2[j])
                    flag=True
                    break
                j+=1
            if flag==False:
                ans.append(-1)
            i+=1
        return ans