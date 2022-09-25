class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            left=0
            right=len(words[i])-1
            tmp=words[i]
            while(left<=right):
                if tmp[left]==tmp[right]:
                    result=words[i]
                else:
                    result=""
                    break
                left+=1
                right-=1
            if(result==words[i]):
                return words[i]
        return result            
     