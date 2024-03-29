class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dicts = {}
        count = 0
        for num in nums:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1
        for num in nums:
            if num+k in dicts:
                count += dicts[num+k]
        return count