class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                currentChar=stack.pop()
                if currentChar=='(':
                    if char!=')':
                        return False
                if currentChar=='{':
                    if char!='}':
                        return False
                if currentChar=='[':
                    if char!=']':
                        return False
        if len(stack)==0:
            return True
        else:
            return False