import sys
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = nums[0]
        second = -sys.maxsize
        third = -sys.maxsize
        if(len(nums)<3):
            return max(nums)
        for i in range(1, len(nums)):
            if (nums[i] > first):
                third = second
                second = first
                first = nums[i]
                print(first,second,third,"if part")
                
            elif first>nums[i]>second: 

                third = second
                second = nums[i]
                print(first,second,third,"1st elif part")

            elif first>nums[i] and second>nums[i] and third<nums[i]:
                third = nums[i]
                print(first,second,third,"2nd elif part")
        if second==third and second==-(2**32):
            third=first
            second=first
        elif third==-(sys.maxsize):
            third=first
        return third