******************O(n^2) method******************************
{
for(i loop)
for(j loop)
#primary diagonal
if i==j
#secondary diagonal
if(i+j)==n-1
}
*******************O(n) method *****************************
{
for(i loop)
#primary diagonal
mat[i][i]
#secondary diagonal
if n-1-i !=i
mat[i][n-1-i]
}
​
​