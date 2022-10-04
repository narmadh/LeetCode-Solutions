class Solution:
    def defangIPaddr(self, address: str) -> str:
        str1=""
        for i in address:
            if "." in i:
                str1=str1+"["+ "." + "]"
            else:
                str1=str1+i
        return str1