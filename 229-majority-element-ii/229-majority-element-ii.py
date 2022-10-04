class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [v for v in set(nums) if nums.count(v)>math.floor(len(nums)/3)]