# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            #print(mid)
            if(isBadVersion(mid)):
                r=mid-1
            else:
                l=mid+1
            if (isBadVersion(mid))==True and (isBadVersion(mid-1)==False):
                return mid
        return 1