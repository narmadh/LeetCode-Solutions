class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	hashMap=set()
    	ans=set()
    	for i in range(n):
    	    if arr[i] in hashMap:
    	        ans.add(arr[i])
    	    else:
    	        hashMap.add(arr[i])
    	ans=list(ans)
    	if len(ans)==0:
    	    return [-1]
    	
    	ans.sort()
    	return ans

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends