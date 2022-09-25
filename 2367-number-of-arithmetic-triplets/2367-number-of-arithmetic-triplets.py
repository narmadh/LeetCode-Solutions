class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hashSet=set()
        for i in nums:
            hashSet.add(i)
        i=0
        j=1
        count=0

        while(i<=j and j<len(nums)):
            if(nums[j]-nums[i]<diff):
                j+=1
            elif(nums[j]-nums[i]>diff):
                i+=1
            else:
                if(nums[j]+diff in hashSet):
                    count+=1
                j+=1
                i+=1
        return count