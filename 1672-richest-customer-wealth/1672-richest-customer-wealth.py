class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for i in range(len(accounts)):
            
            val=0
            for j in range(len(accounts[0])):
                val+=accounts[i][j]

            maximum=max(val,maximum)

        return maximum