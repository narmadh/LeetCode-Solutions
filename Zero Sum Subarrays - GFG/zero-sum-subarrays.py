#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        hashMap = {}
        out = []
        count=0
        sum1 = 0
        for i in range(n):
            sum1 += arr[i]
            if sum1 == 0:
                count+=1
            al = []
            if sum1 in hashMap:
                al = hashMap.get(sum1)
                for it in range(len(al)):
                    out.append((al[it] + 1, i))
                    count+=1
            al.append(i)
            hashMap[sum1] = al
        return count
        #return: count of sub-arrays having their sum equal to 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends