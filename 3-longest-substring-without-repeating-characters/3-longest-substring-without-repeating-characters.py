class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet={}
        len=left=right=0
        n = 0    
        for i in s:
            n += 1
        while(right<n):
            if s[right] in hashSet.keys():
                left=max(left,hashSet.get(s[right])+1)
            hashSet[s[right]]=right
            len=max(len,right-left+1)
            right+=1
        return len
        
                
        