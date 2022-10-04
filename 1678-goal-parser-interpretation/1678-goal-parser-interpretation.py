class Solution:
    def interpret(self, command: str) -> str:
        str1=""
        for i in range(len(command)):
            if command[i]=="(" and command[i+1]==")":
                str1=str1+"o"
            elif command[i]=="G":
                str1=str1+"G"
            elif command[i]=="(" and command[i+1]=="a":
                str1=str1+"al"
        return str1