#User function Template for python3
class Solution:
	def helper(self,ind,ans,arr,sum):
	        if ind>=len(arr):
	            ans.append(sum)
	            
	            return ans
	        sum+=arr[ind]
	        self.helper(ind+1,ans,arr,sum)
	        sum-=arr[ind]
	        self.helper(ind+1,ans,arr,sum)
	        return ans
	def subsetSums(self, arr, N):
	    return self.helper(0,[],arr,0)
	
		# code here
	   
	   
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends