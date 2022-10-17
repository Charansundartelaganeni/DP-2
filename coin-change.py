

#TC:O(m*n)
#SC:O(m*n)



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        m = len(coins)  #let the row count be length of coins
        n = amount   #let the column be the amount
        
        dp = [[0 for i in range(n+1)] for j in range (m+1)]  #initially set all the values to zero
        
        for j in range(1,n+1): 
                    
            dp[0][j] = amount + 1   #fill the first row with the given amount
                    
        #traverse through the matrix            
        for i in range(1,m+1): 
            for j in range(1,n+1): 
                
                    
                if j<coins[i-1]:  #no choose, just copy the value above the row and same column
                    
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    
                    dp[i][j] = min (dp[i-1][j], dp[i][j-coins[i-1]]+1)  #choose, that means the min between no choose and go back current column minus the denomination to find the choose value
                  
        result = dp[m][n]  #last row and last column is going to have my answer
        
        if (result > amount): return -1  #if result is greater than amount, then we can't form a denominations
        
        return result #just return the result
        