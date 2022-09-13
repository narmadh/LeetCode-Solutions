class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction={}
        result=[]
        for i in range(len(nums)):
            if target-nums[i]  in diction:
                result.append(i)
                result.append(diction.get(target-nums[i]))
            else:
                diction.__setitem__(nums[i],i)
        return result