class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1 = p2 = 0
        ans = []
        last_inserted = float('inf')
        nums1.sort()
        nums2.sort()
        while p1<len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if nums1[p1] != last_inserted:
                    ans.append(nums1[p1])
                    last_inserted = nums1[p1]
                p1 += 1
                p2 += 1
            else:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
        return ans