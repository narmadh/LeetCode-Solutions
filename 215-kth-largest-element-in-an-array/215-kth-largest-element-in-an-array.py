class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        size=0
        for num in nums:
            heapq.heappush(heap,num)
            size+=1
            if size>k:
                heapq.heappop(heap)
                #size-=1
        return heapq.heappop(heap)
            