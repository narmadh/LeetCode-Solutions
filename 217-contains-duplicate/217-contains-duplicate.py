class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] not in hashmap.keys():
                hashmap[nums[i]]=1
            else:
                return True
        return False